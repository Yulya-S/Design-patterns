from Src.Core.custom_exceptions import custom_exceptions


# методы расчетов оборотов
class turnover_methods:
    # Сумма
    @staticmethod
    def summ(data: list):
        custom_exceptions.type(data, list)
        summ = 0
        for i in data:
            if i.type:
                summ += i.quantity
            else:
                summ -= i.quantity
        return summ
