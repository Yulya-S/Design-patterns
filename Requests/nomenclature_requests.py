from Requests.start_flask import *
from flask import request

from Src.Core.custom_exceptions import custom_exceptions
from Src.data_reposity import data_reposity


# Получение ключей номенклатуры
@app.route("/app/nomenclature/get", methods=["GET"])
def get_nomenclatures_keys(name: str):
    custom_exceptions.type(name, str)
    reposity = data_reposity()
    return f"{list(reposity.data[data_reposity.nomenclature_key()].keys())}"


# Получение номенклатуры
@app.route("/app/nomenclature/get/<name>", methods=["GET"])
def get_nomenclature(name: str):
    custom_exceptions.type(name, str)
    return f"{nomenclature_service.get(name)}"


# удаление номенклатуры
@app.route("/app/nomenclature/delete/<text>", methods=["DELETE"])
def delete_nomenclature(text: str):
    custom_exceptions.type(text, str)
    return f"{nomenclature_service.delete(text)}"


# создание номенклатуры
@app.route("/app/nomenclature/put/<text>", methods=["PUT"])
def put_nomenclature(text: str):
    custom_exceptions.type(text, str)
    return f"{nomenclature_service.put(text)}"


# Изменение номенклатуры
@app.route("/app/nomenclature/patch/<name>", methods=["PATCH"])
def patch_nomenclature(text: str):
    custom_exceptions.type(text, str)
    return f"{nomenclature_service.patch(text)}"
