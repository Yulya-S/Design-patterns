from Requests.start_flask import *
from Src.Core.custom_exceptions import custom_exceptions
from Src.data_reposity_menager import data_reposity_menager

from flask import request


# Сохранение данных в файл
@app.route("/app/dataset/save", methods=["POST"])
def data_save():
    req = request.json
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]
    custom_exceptions.elements_not_in_array(["file_name"], req)
    custom_exceptions.type(req["file_name"], str)
    data_reposity_menager.save("", req["file_name"])


# востановление данных из файла
@app.route("/app/dataset/load", methods=["POST"])
def data_load():
    req = request.json
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]
    custom_exceptions.elements_not_in_array(["file_name"], req)
    custom_exceptions.type(req["file_name"], str)
    data_reposity_menager.load("", req["file_name"])
