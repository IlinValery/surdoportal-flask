from abc import ABC, abstractmethod
from application.gateway.user_gateway import UserGateway
from application.gateway.log_gateway import LogGateway


class Visitor(ABC):

    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """
    @abstractmethod
    def load_user_data(self, element: UserGateway) -> None:
        pass

    @abstractmethod
    def load_log_data(self, element: LogGateway) -> None:
        pass



"""
Еще нужно добавить наследие в UserGateway и LogGateway от VisitorComponent
Далее прописать функцию accept_load_data(self, visitor: Visitor),
где вызвать visitor.load_user_data (у UserGateway) и visitor.load_log_data (у LogGateway)

"""