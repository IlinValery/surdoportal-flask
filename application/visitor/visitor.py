from abc import ABC, abstractmethod
# from application.gateway.user_gateway import UserGateway
# from application.gateway.department_gateway import DepartmentGateway

class Visitor(ABC):

    """
    Интерфейс Посетителя объявляет набор методов посещения, соответствующих
    классам компонентов. Сигнатура метода посещения позволяет посетителю
    определить конкретный класс компонента, с которым он имеет дело.
    """
    @abstractmethod
    def get_user_number(self, element): #UserGateway
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



"""
Еще нужно добавить наследие в UserGateway и LogGateway от VisitorComponent
Далее прописать функцию accept_load_data(self, visitor: Visitor),
где вызвать visitor.load_user_data (у UserGateway) и visitor.load_log_data (у LogGateway)

"""