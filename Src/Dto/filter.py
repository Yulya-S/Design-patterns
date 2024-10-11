from Src.Core.comparison_format import comparison_format


class formats:
    __name: comparison_format = comparison_format.EQUAL
    __id: comparison_format = comparison_format.EQUAL

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: comparison_format):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: comparison_format):
        self.__id = value


class filter_model:
    __name: str = ""
    __id: str = ""
    __formats: formats = None

    def __init__(self):
        self.__formats = formats()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def formats(self):
        return self.__formats