from Requests.start_flask import *

from flask import request
from datetime import datetime

from Src.data_reposity import data_reposity
from Src.Core.custom_exceptions import custom_exceptions
from Src.models.Warehouse.turnover_creater_manager import turnover_creater_manager
from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.logic.observe_service import observe_service
from Src.Dto.filter_JSON_deserialization import filter_json_deserialization
from Src.Core.event_type import event_type


# Получение даты блокировки
@app.route("/api/warehouse/block_period", methods=['GET'])
def get_block_period():
    return f"{manager.settings.block_period.date()}"


# Установка даты блокировки
@app.route("/app/warehouse/block_period/<data>", methods=["POST"])
def set_block_period(data: str):
    custom_exceptions.type(data, str)
    d = datetime.strptime(data, "%d-%m-%Y")
    observe_service.raise_event(event_type.CHANGE_BLOCK_PERIOD, ["block_period", d])


# получение оборотов
@app.route("/app/warehouse/get_turnover", methods=["POST"])
def get_turnover():
    req = request.json
    custom_exceptions.type(req, dict)
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]

    result = turnover_creater_manager.create_turnover_with_JSON(req)
    return f"{result.turnover}"


# получение транзакций
@app.route("/app/warehouse/get_transactions", methods=["POST"])
def get_transactions():
    req = request.json
    custom_exceptions.type(req, dict)
    if "items" not in list(req.keys()):
        custom_exceptions.other_exception("Были получены некоректные данные!")
    if len(req["items"]) == 0:
        custom_exceptions.other_exception("Полученные данные пусты!")
    req = req["items"][0]

    filter = filter_json_deserialization()
    filter.read_data(req)
    data = reposity.data[data_reposity.transaction_key()]
    prototype = nomenclature_prototype(data)
    result = prototype.create(data, filter.result)
    return f"{result.data}"
