# Обработчики ошибок
class custom_exceptions(Exception):
    # неравенство количества объектов
    @staticmethod
    def length_noequal(resulting_length, estimated_length: int):
        if len(resulting_length) != estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} != {estimated_length}")

    # Количество объектов больше предполагающегося
    @staticmethod
    def length_more(resulting_length, estimated_length: int):
        if len(resulting_length) > estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} > {estimated_length}")

    # не соответствие типу
    @staticmethod
    def type(resulting_type, estimated_type):
        if not isinstance(resulting_type, estimated_type):
            raise custom_exceptions(f"Некорректно передан параметр! {type(resulting_type)} != {estimated_type}")

    # отсутствие ключа в словаре
    @staticmethod
    def presence_element_in_dict(data: dict, key_name: str):
        if key_name not in list(data.keys()):
            raise custom_exceptions(f"Ключь {key_name} отсутствует в словаре!")

    # Получен None вместо значение
    @staticmethod
    def None_received(parameter):
        if parameter is None:
            raise custom_exceptions(f"Был возвращен None вместо значения переменной!")

    # Какой-либо из элементов отсутствует в списке
    @staticmethod
    def elements_not_in_array(elements: list, array):
        custom_exceptions.type(elements, list)
        for i in elements:
            if i not in array:
                raise custom_exceptions(f"Элемент {i} отсутствует в списке {array}!")

    # Проверка соответствия типов элементов списка
    @staticmethod
    def elements_is_type(elements: list, type):
        custom_exceptions.type(elements, list)
        for i in elements:
            custom_exceptions.type(i, type)

    # Какая либо другая ошибка
    @staticmethod
    def other_exception(text: str):
        raise custom_exceptions(f"{text}")
