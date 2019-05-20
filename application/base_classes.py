from abc import ABC, abstractmethod

class UserBase(ABC):
    def __init__(self, user_id=None, user_email=str(), user_fn=str(), user_sn=str(), user_pass="secret_pass", user_su=0):
        self.id = user_id
        self.email = user_email
        self.first_name = user_fn
        self.last_name = user_sn
        self.password = user_pass
        self.is_superuser = user_su


class TermBase(ABC):
    def __init__(self, term_id=int(), term_caption=str(), term_description=str(), term_lesson=int(), term_teacher=int(),
                 term_discipline=int(), term_image=str(), term_creator=int(), term_changed=str(), term_is_shown=0):
        self.id = term_id
        self.caption = term_caption
        self.description = term_description
        self.lesson = term_lesson
        self.teacher = term_teacher
        self.discipline = term_discipline
        self.image_path = term_image
        self.creator = term_creator
        self.changed = term_changed
        self.is_shown = term_is_shown


class MediaBase(ABC):
    """ Class for term's video media content
    Constructor get parameters of this class """
    def __init__(self, media_id=None, media_type=str(), media_youtube_id=str(), media_to_term=int()):
        self.id = media_id
        self.type = media_type
        self.youtube_id = media_youtube_id
        self.to_term = media_to_term


class TeacherBase(ABC):
    def __init__(self, teacher_id=None, teacher_name=str(), teacher_to_department=int()):
        self.id = teacher_id
        self.name = teacher_name
        self.department = teacher_to_department


class DisciplineBase(ABC):
    def __init__(self, discipline_id=None, discipline_name=str(), discipline_semester=int(),
                 discipline_to_department=int()):
        self.id = discipline_id
        self.name = discipline_name
        self.semester = discipline_semester
        self.department = discipline_to_department



class DepartmentBase(ABC):
    def __init__(self, department_id=None, department_name=str(), department_initials=str()):
        self.id = department_id
        self.caption = department_name
        self.initials = department_initials


class LogBase(ABC):
    def __init__(self, log_date=str(), log_table=str(), log_element_id=int(), log_action=str(), log_user_id=int()):
        self.date = log_date
        self.user = log_user_id
        self.table = log_table
        self.element = log_element_id
        self.action = log_action
