class custom_exceptions(Exception):
    def length_noequal(self, resulting_length, estimated_length: int):
        if len(resulting_length) != estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} != {estimated_length}")

    def length_more(self, resulting_length, estimated_length: int):
        if len(resulting_length) > estimated_length:
            raise custom_exceptions(f"Неверная длина параметра! {len(resulting_length)} > {estimated_length}")

    def type(self, resulting_type, estimated_type):
        if not isinstance(resulting_type, estimated_type):
            raise custom_exceptions(f"Некорректно передан параметр! {type(resulting_type)} != {estimated_type}")

    def None_received(self, parameter):
        if parameter is None:
            raise custom_exceptions(f"Был возвращен None вместо значения переменной!")

    def other_exception(self, text: str):
        raise custom_exceptions(f"{text}")
