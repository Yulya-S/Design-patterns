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
    def None_received(parameter):
        if parameter is None:
            raise custom_exceptions(f"Был возвращен None вместо значения переменной!")

    @staticmethod
    def other_exception(text: str):
        raise custom_exceptions(f"{text}")
