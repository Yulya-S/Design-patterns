from Src.settings_manager import settings_manager
from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.Reports.report_factory import report_factory
from Src.Core.formats_and_methods.format_reporting import format_reporting
from Src.Reports.csv_report import csv_report
from Src.Reports.markdown_report import markdown_report
from Src.Reports.json_report import json_report
from Src.Reports.xml_report import xml_report
from Src.Reports.rtf_report import rtf_report
from Src.Json_deserialization import json_deserialization

import unittest


class test_reporting(unittest.TestCase):
    # Проверка работы отчета CSV
    def test_csv_report_create_range(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = csv_report()

        # Действие
        report.create(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # Проверка работы отчета CSV
    def test_csv_report_create_nomenclature(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = csv_report()

        # Действие
        report.create(reposity.data[data_reposity.nomenclature_key()])

        # Проверки
        assert report.result != ""

    # Проверить работу фабрики для получения инстанса нужного отчета
    def test_report_factory_create_csv_report(self):
        # Подготовка
        manager = settings_manager()
        start = start_service()
        start.create()

        # Действие
        report = report_factory(manager.settings).create(format_reporting.CSV)

        # Проверки
        assert report is not None
        assert isinstance(report, csv_report)

    # создание тестового файла отчета CSC
    def test_csv_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = csv_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.nomenclature_key()],
                              file_name="test_csv_report_upload_to_file")

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета MARKDOWN
    def test_markdown_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = markdown_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()], file_name="test_markdown_report_upload_to_file")

        # Проверки
        assert report.result != ""

    # создание отчета JSON по данным group
    def test_json_report_upload_to_file_group(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.group_key()], file_name="test_json_report_group")

        # Проверки
        assert report.result != ""

    # создание отчета JSON по данным receipt
    def test_json_report_upload_to_file_receipt(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.receipt_key()], file_name="test_json_report_receipt")

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета XML
    def test_xml_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = xml_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.receipt_key()], file_name="test_xml_report_upload_to_file")

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета RTF
    def test_rtf_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = rtf_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()], file_name="test_rtf_report_upload_to_file")

        # Проверки
        assert report.result != ""

    # создание стандартнго шаблона отчета
    def test_report_factory_create_default(self):
        # Подготовка
        manager = settings_manager()
        start = start_service()
        start.create()
        report = report_factory(manager.settings)

        # Действие
        result = report.create_default

        # Проверки
        assert result is not None
        assert isinstance(result, csv_report)

    # десериализация из JSON значений group
    def test_report_deserialization_qroup(self):
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()
        deserialization = json_deserialization()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.group_key()], file_name="test_json_report_group")
        result = deserialization.group_from_JSON("test_json_report_group.json", "..\\Docs\\reports")
        d1 = start.reposity.data[reposity.group_key()]

        # Проверки
        assert d1[0] == result[0]
        assert d1[0].name == result[0].name

    # десериализация из JSON значений range
    def test_report_deserialization_range(self):
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()
        deserialization = json_deserialization()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()], file_name="test_json_report_range")
        result = deserialization.range_from_JSON("test_json_report_range.json", "..\\Docs\\reports")
        d1 = start.reposity.data[reposity.range_key()]

        # Проверки
        assert d1[list(d1.keys())[0]] == result[list(result.keys())[0]]
        assert d1[list(d1.keys())[0]].base == result[list(result.keys())[0]].base
        assert d1[list(d1.keys())[0]].name == result[list(result.keys())[0]].name
        assert d1[list(d1.keys())[0]].conversion_factor == result[list(result.keys())[0]].conversion_factor

    # десериализация из JSON значений nomenclature
    def test_report_deserialization_nomenclature(self):
        # Подготовка
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()
        deserialization = json_deserialization()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.nomenclature_key()],
                              file_name="test_json_report_nomenclature")
        result = deserialization.nomenclature_from_JSON("test_json_report_nomenclature.json", "..\\Docs\\reports")
        d1 = start.reposity.data[reposity.nomenclature_key()]

        # Проверки
        assert d1[list(d1.keys())[0]] == result[list(result.keys())[0]]
        assert d1[list(d1.keys())[0]].full_name == result[list(result.keys())[0]].full_name
        assert d1[list(d1.keys())[0]].name == result[list(result.keys())[0]].name
        assert d1[list(d1.keys())[0]].nomenclature_group == result[list(result.keys())[0]].nomenclature_group
        assert d1[list(d1.keys())[0]].range == result[list(result.keys())[0]].range

    # десериализация из JSON значений receipt
    def test_report_deserialization_receipt(self):
        reposity = data_reposity()
        start = start_service()
        start.create()
        report = json_report()
        deserialization = json_deserialization()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.receipt_key()], file_name="test_json_report_receipt")
        result = deserialization.receipts_from_JSON("test_json_report_receipt.json", "..\\Docs\\reports")
        d1 = start.reposity.data[reposity.receipt_key()]

        # Проверки
        assert d1[0] == result[0]
        assert d1[0].name == result[0].name
        assert d1[0].steps_cooking == result[0].steps_cooking
        assert d1[0].cooking_time == result[0].cooking_time
        assert d1[0].number_servings == result[0].number_servings
        assert d1[0].ingredients == result[0].ingredients
