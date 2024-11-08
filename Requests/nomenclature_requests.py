from Requests.start_flask import *
from flask import request

from Src.Core.custom_exceptions import custom_exceptions


# Получение номенклатуры
@app.route("/app/nomenclature/get/<name>", methods=["GET"])
def get_nomenclature(name: str):
    custom_exceptions.type(name, str)
    return f"{nomenclature_service.get(name)}"


# удаление номенклатуры
@app.route("/app/nomenclature/delete/<name>", methods=["DELETE"])
def delete_nomenclature(name: str):
    custom_exceptions.type(name, str)
    return f"{nomenclature_service.delete(name)}"


# создание номенклатуры
@app.route("/app/nomenclature/put/<name>", methods=["PUT"])
def put_nomenclature(name: str):
    req = request.json
    custom_exceptions.type(req, dict)
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]
    custom_exceptions.elements_not_in_array(["range_name", "group_name"], list(req.keys()))
    return f"{nomenclature_service.put(name, req['group_name'], req['range_name'])}"


# Изменение номенклатуры
@app.route("/app/nomenclature/patch/<name>", methods=["PATCH"])
def patch_nomenclature(name: str):
    req = request.json
    custom_exceptions.type(req, dict)
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]
    custom_exceptions.elements_not_in_array(["range_name", "group_name"], list(req.keys()))
    return f"{nomenclature_service.patch(name, req['group_name'], req['range_name'])}"
