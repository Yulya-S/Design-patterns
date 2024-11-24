from Requests.start_flask import *

from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type
from Src.logic.observe_service import observe_service
from Src.data_reposity import data_reposity


# Получение ключей номенклатуры
@app.route("/app/nomenclature/get", methods=["GET"])
def get_nomenclatures_keys(name: str):
    try:
        custom_exceptions.type(name, str)
        reposity = data_reposity()
        observe_service.raise_event(event_type.INFO_LOG, "GET /app/nomenclature/get TRUE")
        return f"{list(reposity.data[data_reposity.nomenclature_key()].keys())}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Получение номенклатуры
@app.route("/app/nomenclature/get/<name>", methods=["GET"])
def get_nomenclature(name: str):
    try:
        custom_exceptions.type(name, str)
        observe_service.raise_event(event_type.INFO_LOG, f"GET /app/nomenclature/get/{name} TRUE")
        return f"{nomenclature_service.get(name)}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# удаление номенклатуры
@app.route("/app/nomenclature/delete/<text>", methods=["DELETE"])
def delete_nomenclature(text: str):
    try:
        custom_exceptions.type(text, str)
        observe_service.raise_event(event_type.INFO_LOG, f"DELETE /app/nomenclature/delete/{text} TRUE")
        return f"{nomenclature_service.delete(text)}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# создание номенклатуры
@app.route("/app/nomenclature/put/<text>", methods=["PUT"])
def put_nomenclature(text: str):
    try:
        custom_exceptions.type(text, str)
        observe_service.raise_event(event_type.INFO_LOG, f"PUT /app/nomenclature/put/{text} TRUE")
        return f"{nomenclature_service.put(text)}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# Изменение номенклатуры
@app.route("/app/nomenclature/patch/<name>", methods=["PATCH"])
def patch_nomenclature(text: str):
    try:
        custom_exceptions.type(text, str)
        observe_service.raise_event(event_type.INFO_LOG, f"PATCH /app/nomenclature/path/{text} TRUE")
        return f"{nomenclature_service.patch(text)}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)