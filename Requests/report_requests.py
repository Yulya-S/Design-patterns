from Requests.start_flask import *

from flask import request
from datetime import datetime

from Src.data_reposity import data_reposity
from Src.Dto.filter import filter_model

from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Core.event_type import event_type
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.formats_and_methods.comparison_format import comparison_format

from Src.Reports.report_factory import report_factory
from Src.Reports.OBS.tbs_calculation import tbs_calculation

from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.logic.observe_service import observe_service


# получение оборотно-сальдовая ведомость
@app.route("/api/reports/tbs", methods=['GET'])
def get_tbs():
    try:
        req = request.json
        if "items" not in list(req.keys()):
            custom_exceptions.other_exception("Были получены некоректные данные!")
        if len(req["items"]) == 0:
            custom_exceptions.other_exception("Полученные данные пусты!")
        req = req["items"][0]
        custom_exceptions.elements_not_in_array(["begin", "end", "warehouse_code"], req)

        warehouse = None
        for i in reposity.data[data_reposity.warehouse_key()]:
            if i.unique_code == req["warehouse_code"]:
                warehouse = i
                break
        custom_exceptions.None_received(warehouse)
        tbs = tbs_calculation([datetime.strptime(req["begin"], "%d-%m-%Y"),
                               datetime.strptime(req["end"], "%d-%m-%Y")], warehouse)
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/reports/tbs TRUE")
        return f"{tbs.result}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# получение списка форматов для фильтрации
@app.route("/api/reports/comparison_formats", methods=['GET'])
def c_formats():
    try:
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/reports/comparison_formats TRUE")
        return comparison_format.list()
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)

# Получение ключей репозитория
@app.route("/api/reports/model_names", methods=['GET'])
def model_names():
    try:
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/reports/model_names TRUE")
        return data_reposity.keys()
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)

# получение отчета с использованием фильтров
@app.route("/app/reports/<entity>", methods=["POST"])
def filter_with_filter(entity: str):
    try:
        custom_exceptions.type(entity, str)
        if entity not in data_reposity.keys():
            custom_exceptions.other_exception("Некорректно указан тип данных! См метод /api/report/entities")

        req = request.json
        custom_exceptions.type(req, dict)
        if "items" not in list(req.keys()):
            custom_exceptions.other_exception("Были получены некоректные данные!")
        if len(req["items"]) == 0:
            custom_exceptions.other_exception("Полученные данные пусты!")
        req = req["items"][0]
        custom_exceptions.elements_not_in_array(["field", "comparison_format", "value"], list(req.keys()))

        filter = filter_model()
        filter.update_filter(req['field'], comparison_format(req["comparison_format"]), req["value"])

        data = reposity.data[entity]
        if type(data) == dict:
            dd = list()
            for i in list(data.keys()):
                dd.append(data[i])
            data = dd

        prototype = nomenclature_prototype(data)
        result = prototype.create(data, filter)

        factory = report_factory(manager.settings)
        report = factory.create_default
        report.create(result.data)
        if report is None:
            raise custom_exceptions.other_exception("Невозможно подобрать корректный отчет согласно параметрам!")

        report.create(result.data)
        observe_service.raise_event(event_type.INFO_LOG, f"POST /app/reports/{entity} TRUE")
        return report.result
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получить список форматов отчетов
@app.route("/api/reports/formats", methods=['GET'])
def formats():
    try:
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/reports/formats TRUE")
        return format_reporting.list()
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получить отчет по списоку единиц измерения
@app.route("/app/reports/ranges/<format>", methods=["GET"])
def reportRanges(format: int):
    try:
        custom_exceptions.type(format, int)
        if not format_reporting.check(format):
            raise custom_exceptions.other_exception("Некорректно указан формат отчета! См метод /api/report/formats")

        factory = report_factory(manager.settings)
        report_format = format_reporting(format)
        report = factory.create(report_format)

        if report is None:
            raise custom_exceptions.other_exception("Невозможно подобрать корректный отчет согласно параметрам!")

        if len(reposity.data) == 0:
            raise custom_exceptions.other_exception("Набор данных пуст!")

        report.create(reposity.data[data_reposity.range_key()])
        observe_service.raise_event(event_type.INFO_LOG, f"GET /app/reports/ranges/{format} TRUE")
        return report.result
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получить отчет по списоку групп
@app.route("/app/reports/groups/<format>", methods=["GET"])
def reportGroups(format: int):
    try:
        custom_exceptions.type(format, int)
        if not format_reporting.check(format):
            raise custom_exceptions.other_exception("Некорректно указан формат отчета! См метод /api/report/formats")

        factory = report_factory(manager.settings)
        report_format = format_reporting(format)
        report = factory.create(report_format)

        if report is None:
            raise custom_exceptions.other_exception("Невозможно подобрать корректный отчет согласно параметрам!")

        if len(reposity.data) == 0:
            raise custom_exceptions.other_exception("Набор данных пуст!")

        report.create(reposity.data[data_reposity.group_key()])
        observe_service.raise_event(event_type.INFO_LOG, f"GET /app/reports/groups/{format} TRUE")
        return report.result
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получить отчет по списоку номенклатуры
@app.route("/app/reports/nomenclatures/<format>", methods=["GET"])
def reportNomenclatures(format: int):
    try:
        custom_exceptions.type(format, int)
        if not format_reporting.check(format):
            raise custom_exceptions.other_exception("Некорректно указан формат отчета! См метод /api/report/formats")

        factory = report_factory(manager.settings)
        report_format = format_reporting(format)
        report = factory.create(report_format)

        if report is None:
            raise custom_exceptions.other_exception("Невозможно подобрать корректный отчет согласно параметрам!")

        if len(reposity.data) == 0:
            raise custom_exceptions.other_exception("Набор данных пуст!")

        report.create(reposity.data[data_reposity.nomenclature_key()])
        observe_service.raise_event(event_type.INFO_LOG, f"GET /app/reports/nomenclatures/{format} TRUE")
        return report.result
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получить отчет по списоку рецептов
@app.route("/app/reports/receipts/<format>", methods=["GET"])
def reportReceipts(format: int):
    try:
        custom_exceptions.type(format, int)
        if not format_reporting.check(format):
            raise custom_exceptions.other_exception("Некорректно указан формат отчета! См метод /api/report/formats")

        factory = report_factory(manager.settings)
        report_format = format_reporting(format)
        report = factory.create(report_format)

        if report is None:
            raise custom_exceptions.other_exception("Невозможно подобрать корректный отчет согласно параметрам!")

        if len(reposity.data) == 0:
            raise custom_exceptions.other_exception("Набор данных пуст!")

        report.create(reposity.data[data_reposity.receipt_key()])
        observe_service.raise_event(event_type.INFO_LOG, f"GET /app/reports/receipts/{format} TRUE")
        return report.result
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)
