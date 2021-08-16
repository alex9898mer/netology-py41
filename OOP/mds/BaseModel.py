from typing import List, Dict


class Base:
    def __init__(self, name, surname, gender=None):
        self.name: str = name
        self.surname: str = surname
        self.gender: str = gender if gender else "male"
        self.courses_attached: List[str] = []
        self.grades: Dict[str, List[int]] = {}

    def attach_course(self, course_name):
        raise NotImplementedError

    def course_exists(self, course_name):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError
