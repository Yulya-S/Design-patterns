class custom_exceptions(Exception):
    @staticmethod
    def length_noequal(resulting_length, estimated_length: int):
        if len(resulting_length) != estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} != {estimated_length}")

    @staticmethod
    def length_more(resulting_length, estimated_length: int):
        if len(resulting_length) > estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} > {estimated_length}")

    @staticmethod
    def type(resulting_type, estimated_type):
        if not isinstance(resulting_type, estimated_type):
            raise custom_exceptions(f"Некорректно передан параметр! {type(resulting_type)} != {estimated_type}")

    @staticmethod
    def presence_element_in_dict(data: dict, key_name: str):
        if key_name not in list(data.keys()):
            raise custom_exceptions(f"Ключь {key_name} отсутствует в словаре!")

    @staticmethod
    def None_received(parameter):
        if parameter is None:
            raise custom_exceptions(f"Был возвращен None вместо значения переменной!")

    @staticmethod
    def elements_not_in_array(elements, array):
        for i in elements:
            if i not in array:
                raise custom_exceptions(f"Элемент {i} отсутствует в списке {array}!")

    @staticmethod
    def other_exception(text: str):
        raise custom_exceptions(f"{text}")
