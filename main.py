import connexion
from flask import request

from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.Dto.filter import filter_model

from Src.Core.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.comparison_format import comparison_format

from Src.models.Warehouse.warehouse_model import warehouse_model
from Src.Reports.report_factory import report_factory
from Src.logic.nomenclature_prototype import nomenclature_prototype

app = connexion.FlaskApp(__name__)
app.add_api("swagger.yaml")

reposity = data_reposity()
manager = settings_manager()
manager.open("settings.json")
receipt = receipt_book_menager()
start = start_service()

start.create(".")


@app.route("/app/get_transactions", methods=["POST"])
def get_transactions():
    req = request.json
    custom_exceptions.type(req, dict)
    req = request.json
    custom_exceptions.type(req, dict)
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]
    custom_exceptions.elements_not_in_array(["nomenclature", "warehouse"], list(req.keys()))
    for i in list(req.keys()):
        custom_exceptions.elements_not_in_array(["comparison_format", "value"], list(req[i].keys()))

    data = reposity.data[data_reposity.transaction_key()]
    filter = filter_model()
    for i in list(req.keys()):
        if i != "" and i != None:
            if i == "nomenclature":
                req[i]["value"] = reposity.data[data_reposity.nomenclature_key()][req[i]["value"]]
            elif i == "warehouse":
                wh = warehouse_model(req[i]["value"])
                for l in reposity.data[data_reposity.warehouse_key()]:
                    if l == wh:
                        req[i]["value"] = l
        filter.update_filter(i, comparison_format(req[i]["comparison_format"]), req[i]["value"])
    prototype = nomenclature_prototype(data)
    result = prototype.create(data, filter)
    return f"{result.data}"


@app.route("/api/reports/comparison_formats", methods=['GET'])
def c_formats():
    return comparison_format.list()


@app.route("/api/reports/model_names", methods=['GET'])
def model_names():
    return data_reposity.keys()


@app.route("/app/reports/<entity>", methods=["POST"])
def filter_with_filter(entity: str):
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
    return report.result


"""
Получить список форматов отчетов
"""


@app.route("/api/reports/formats", methods=['GET'])
def formats():
    return format_reporting.list()


# Получить отчет по списоку единиц измерения
@app.route("/app/reports/ranges/<format>", methods=["GET"])
def reportRanges(format: int):
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
    return report.result


# Получить отчет по списоку групп
@app.route("/app/reports/groups/<format>", methods=["GET"])
def reportGroups(format: int):
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
    return report.result


# Получить отчет по списоку номенклатуры
@app.route("/app/reports/nomenclatures/<format>", methods=["GET"])
def reportNomenclatures(format: int):
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
    return report.result


# Получить отчет по списоку рецептов
@app.route("/app/reports/receipts/<format>", methods=["GET"])
def reportReceipts(format: int):
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
    return report.result


if __name__ == '__main__':
    app.run(port=8080)
