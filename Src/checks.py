def type_check(value, intended_type):
    if not isinstance(value, intended_type):
        raise TypeError(
            f"Передана переменная неверного типа! предполагался {intended_type} был получен {type(value)}")


def value_check(condition: bool):
    if not condition:
        raise ValueError(f"Передано неверное значение переменной!")