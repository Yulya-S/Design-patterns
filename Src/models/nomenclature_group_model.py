from Src.abstract_model import abstract_model


class nomenclature_group_model(abstract_model):
    def set_compare_mode(self, other, equal: bool = True) -> bool:
        return super().set_compare_mode(other, equal)
