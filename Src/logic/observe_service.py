from Src.Core.Abstract_classes.abstract_logic import abstract_logic
from Src.Core.custom_exceptions import custom_exceptions
from Src.Core.event_type import event_type


# обработчик событий
class observe_service:
    __observers = []

    @staticmethod
    def append(service: abstract_logic):
        if service is None:
            return
        custom_exceptions.type(service, abstract_logic)
        items = list(map(lambda x: type(x).__name__, observe_service.__observers))
        found = type(service).__name__ in items
        if not found:
            observe_service.__observers.append(service)

    @staticmethod
    def raise_event(type: event_type, params):
        for instance in observe_service.__observers:
            if instance is not None:
                instance.handle_event(type, params)
