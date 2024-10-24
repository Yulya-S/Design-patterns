from Src.Core.base_models import base_model_name, base_model_code


class filter_metods:
    @staticmethod
    def equal_in_fragment(source, field: str, text: any):
        if type(source) == list:
            for i in source:
                if filter_metods.equal_in_fragment(i, field, text):
                    return True
        elif type(source) == dict:
            for i in list(source.keys()):
                if filter_metods.equal_in_fragment(source[i], field, text):
                    return True
        elif issubclass(type(source), base_model_name) or issubclass(type(source), base_model_code):
            for i in dir(source):
                if filter_metods.equal_in_fragment(source.__getattribute__(i), field, text):
                    return True
            if field in dir(source):
                return source.__getattribute__(field) == text
        return False

    @staticmethod
    def equals(source: list, field: str, text: any, look_inside: bool = False):
        if text == "" or text == None:
            return source
        result = []
        for item in source:
            if item.__getattribute__(field) == text or (
                    look_inside and filter_metods.equal_in_fragment(item, field, text)):
                result.append(item)
        return result

    @staticmethod
    def like_in_fragment(source, field: str, text: any):
        if type(source) == list:
            for i in source:
                if filter_metods.like_in_fragment(i, field, text):
                    return True
        elif type(source) == dict:
            for i in list(source.keys()):
                if filter_metods.like_in_fragment(source[i], field, text):
                    return True
        elif issubclass(type(source), base_model_name) or issubclass(type(source), base_model_code):
            for i in dir(source):
                if filter_metods.like_in_fragment(source.__getattribute__(i), field, text):
                    return True
            if field in dir(source):
                return text in source.__getattribute__(field)
        return False

    @staticmethod
    def like(source: list, field: str, text: any, look_inside: bool = False):
        if text == "" or text == None:
            return source
        result = []
        for item in source:
            if text in item.__getattribute__(field) or (
                    look_inside and filter_metods.like_in_fragment(item, field, text)):
                result.append(item)
        return result
