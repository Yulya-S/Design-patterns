from Src.settings_manager import settings_manager
from Src.receipt_book_menager import receipt_book_menager
from Src.data_reposity import data_reposity
from Src.start_service import start_service
from Src.Reports.report_factory import report_factory
from Src.Core.format_reporting import format_reporting
from Src.Reports.csv_report import csv_report
from Src.Reports.markdown_report import markdown_report

import unittest


class test_reporting(unittest.TestCase):
    def test_csv_report_create(self):
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

    def test_report_factory_create_markdown_report(self):
        # Подготовка
        reposity = data_reposity()
        manager = settings_manager()
        receipt = receipt_book_menager()
        start = start_service(reposity, manager, receipt)
        start.create()

        # Действие
        report = report_factory().create(format_reporting.MARCDOWN)

        # Проверки
        assert report is not None
        assert isinstance(report, markdown_report)
