from Src.abstract_model import abstract_model


class nomenclature_group_model(abstract_model):
    def __eq__(self, other):
        return self._equal(other)

    def __ne__(self, other):
        return self._noequal(other)
