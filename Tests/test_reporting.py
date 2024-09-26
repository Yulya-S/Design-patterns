from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.Reports.report_factory import report_factory
from Src.Core.format_reporting import format_reporting
from Src.Reports.csv_report import csv_report
from Src.Reports.markdown_report import markdown_report
from Src.Reports.json_report import json_report
from Src.Reports.xml_report import xml_report
from Src.Reports.rtf_report import rtf_report

import unittest


class test_reporting(unittest.TestCase):
    # Проверка работы отчета CSV
    def test_csv_report_create_range(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = csv_report()

        # Действие
        report.creat(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # Проверка работы отчета CSV
    def test_csv_report_create_nomenclature(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = csv_report()

        # Действие
        report.creat(reposity.data[data_reposity.nomenclature_key()])

        # Проверки
        assert report.result != ""

    # Проверить работу фабрики для получения инстанса нужного отчета
    def test_report_factory_create_csv_report(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()

        # Действие
        report = report_factory().create(format_reporting.CSV)

        # Проверки
        assert report is not None
        assert isinstance(report, csv_report)

    # создание тестового файла отчета CSC
    def test_csv_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = csv_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета MARKDOWN
    def test_markdown_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = markdown_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета JSON
    def test_json_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = json_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета XML
    def test_xml_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = xml_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""

    # создание тестового файла отчета RTF
    def test_rtf_report_upload_to_file(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()
        report = rtf_report()

        # Действие
        report.upload_to_file(reposity.data[data_reposity.range_key()])

        # Проверки
        assert report.result != ""