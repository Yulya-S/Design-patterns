from Src.Core.abstract_prototipe import abstract_prototype
from Src.Dto.filter import filter_model
from Src.logic.prototype_factory import prototype_factory
from Src.Core.comparison_format import comparison_format


class nomenclature_prototype(abstract_prototype):
    def __init__(self, source: list) -> None:
        super().__init__(source)

    def create(self, data: list, filterDto: filter_model, look_inside: bool = False):
        super().create(data, filterDto)
        self.data = self.filter_name(self.data, filterDto, look_inside)
        self.data = self.filter_id(self.data, filterDto, look_inside)
        self.data = self.filter_warehouse(self.data, filterDto, look_inside)
        self.data = self.filter_nomenclature(self.data, filterDto, look_inside)
        instance = nomenclature_prototype(self.data)
        return instance

    def filter_name(self, source: list, filterDto: filter_model, look_inside: bool = False) -> list:
        comparison = prototype_factory.get(filterDto.formats.get("name"))
        return comparison(source, "name", filterDto.name, look_inside)

    def filter_id(self, source: list, filterDto: filter_model, look_inside: bool = False) -> list:
        comparison = prototype_factory.get(filterDto.formats.get("id"))
        return comparison(source, "id", filterDto.id, look_inside)

    def filter_warehouse(self, source: list, filterDto: filter_model, look_inside: bool = False) -> list:
        comparison = prototype_factory.get(filterDto.formats.get("warehouse"))
        return comparison(source, "warehouse", filterDto.warehouse, look_inside)

    def filter_nomenclature(self, source: list, filterDto: filter_model, look_inside: bool = False) -> list:
        comparison = prototype_factory.get(filterDto.formats.get("nomenclature"))
        return comparison(source, "nomenclature", filterDto.nomenclature, look_inside)

    def filter_periods(self, source: list, filterDto: filter_model) -> list:
        comparison = prototype_factory.get(comparison_format.RANGE)
        return comparison(source, filterDto.periods[0], filterDto.periods[1])
