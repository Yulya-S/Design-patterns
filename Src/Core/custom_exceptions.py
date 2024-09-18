class custom_exceptions(Exception):
    def length(self, resulting_length: int, estimated_length: int, operator: str):
        return custom_exceptions(f"Неверная длина параметра! {resulting_length} {operator} {estimated_length}")

    def type(self, resulting_type, estimated_type):
        return custom_exceptions(f"Некорректно передан параметр! {resulting_type} != {estimated_type}")
