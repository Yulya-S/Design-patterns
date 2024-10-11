import re
import connexion

from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager

from Src.Core.format_reporting import format_reporting
from Src.Core.custom_exceptions import custom_exceptions

from Src.Reports.report_factory import report_factory

# from Src.settings_manager import settings_manager
# from Src.Reports.report_factory import report_factory

app = connexion.FlaskApp(__name__)
app.add_api("swagger.yaml")

reposity = data_reposity()
manager = settings_manager()
manager.open("settings.json")
receipt = receipt_book_menager()
start = start_service(reposity, manager, receipt)
start.create(".")

"""
Получить список форматов отчетов
"""


@app.route("/api/reports/formats", methods=['GET'])
def formats():
    return format_reporting.list()


# Запуск
# @app.route("/")
# def hello():
#     return "Api сервер запущен!"


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
