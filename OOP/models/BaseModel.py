from typing import List, Dict


class Base:
    def __init__(self, name: str, surname: str, gender=None):
        self._name: str = name
        self._surname: str = surname
        self._gender: str = gender if gender else "male"
        self._courses_attached: List[str] = []
        self._grades: Dict[str, List[int]] = {}

    def course_exists(self, course_name: str) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def attach_course(self, course_name: str):
        raise NotImplementedError

    def get_grades(self) -> Dict[str, List[int]]:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_surname(self) -> str:
        raise NotImplementedError

    def get_attached_courses(self) -> List[str]:
        raise NotImplementedError
