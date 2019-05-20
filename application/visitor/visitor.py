from abc import ABC, abstractmethod

class Visitor(ABC):

    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """
    @abstractmethod
    def get_user_number(self, element):
        pass

    @abstractmethod
    def get_department_number(self, element):
        pass

    @abstractmethod
    def get_discipline_number(self, element):
        pass

    @abstractmethod
    def get_teacher_number(self, element):
        pass

    @abstractmethod
    def get_term_number(self, element):
        pass

    @abstractmethod
    def get_media_number(self, element):
        pass

