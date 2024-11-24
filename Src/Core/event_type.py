from enum import Enum


# Типы событий
class event_type(Enum):
    DELETE_NOMENCLATURE = 1
    CHANGE_NOMENCLATURE = 2
    CHANGE_RANGE = 3
    CHANGE_BLOCK_PERIOD = 4
    DEBUG_LOG = 5
    INFO_LOG = 6
    ERROR_LOG = 7
