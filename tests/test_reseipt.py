from Src.receipt_book_menager import receipt_book_menager
import unittest

"""
Набор тестов для проверки добавления рецептов
"""
class test_reseipt(unittest.TestCase):
    def test_reseipts_append_ingredients(self):
        # Подготовка
        reseipts = receipt_book_menager()

        # Проверки
        assert len(reseipts.receipt_book.receipes) == 2
        assert "Соль" in reseipts.receipt_book.receipes[0].get_names_ingredients

