from abc import ABC, abstractmethod
from application.visitor.visitor import Visitor


class VisitorComponent(ABC):
    """
    Интерфейс Компонента объявляет метод accept, который в качестве аргумента
    может получать любой объект, реализующий интерфейс посетителя.
    """
    @abstractmethod
    def access_get_number(self, visitor: Visitor):
        pass
