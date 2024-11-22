from Requests.start_flask import *

from flask import request
from datetime import datetime

from Src.Core.event_type import event_type
from Src.Core.custom_exceptions import custom_exceptions

from Src.logic.nomenclature_prototype import nomenclature_prototype
from Src.logic.observe_service import observe_service

from Src.data_reposity import data_reposity
from Src.models.Warehouse.turnover_creater_manager import turnover_creater_manager
from Src.Dto.filter_JSON_deserialization import filter_json_deserialization


# получение всех складов
@app.route("/api/warehouse", methods=['GET'])
def get_warehouses():
    try:
        reposity = data_reposity()
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/warehouse TRUE")
        return f"{[i.__str__() for i in reposity.data[data_reposity.warehouse_key()]]}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)

# Получение даты блокировки
@app.route("/api/warehouse/block_period", methods=['GET'])
def get_block_period():
    try:
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/warehouse/block_period TRUE")
        return f"{manager.settings.block_period.date()}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)

# Установка даты блокировки
@app.route("/app/warehouse/block_period/<data>", methods=["POST"])
def set_block_period(data: str):
    try:
        custom_exceptions.type(data, str)
        d = datetime.strptime(data, "%d-%m-%Y")
        observe_service.raise_event(event_type.CHANGE_BLOCK_PERIOD, ["block_period", d])
        observe_service.raise_event(event_type.INFO_LOG, f"POST /app/warehouse/block_period/{data} TRUE")
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# получение оборотов
@app.route("/app/warehouse/get_turnover", methods=["POST"])
def get_turnover():
    try:
        req = request.json
        custom_exceptions.type(req, dict)
        if "items" not in list(req.keys()):
            custom_exceptions.other_exception("Были получены некоректные данные!")
        if len(req["items"]) == 0:
            custom_exceptions.other_exception("Полученные данные пусты!")
        req = req["items"][0]

        result = turnover_creater_manager.create_turnover_with_JSON(req)
        observe_service.raise_event(event_type.INFO_LOG, f"POST /app/warehouse/get_turnover TRUE")
        return f"{result.turnover}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)


# получение транзакций
@app.route("/app/warehouse/get_transactions", methods=["POST"])
def get_transactions():
    try:
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
        observe_service.raise_event(event_type.INFO_LOG, f"GET /api/warehouse/get_transactions TRUE")
        return f"{result.data}"
    except Exception as ex:
        observe_service.raise_event(event_type.ERROR_LOG, ex)
