from typing import Dict, List, Union, TYPE_CHECKING
from abc import ABC

from .BaseModel import Base

if TYPE_CHECKING:
    pass


class Student(Base, ABC):
    def __init__(self, name: str, surname: str, gender: Union[str, None] = None):
        super(Student, self).__init__(name, surname, gender)
        self._finished_courses: List[str] = []

    def __str__(self) -> str:
        return (
            f"Имя: {self._name}"
            f"Фамилия: {self._surname}"
            f"Средняя оценка за домашние задания: {self.get_hw_media()}"
            f"Курсы в процессе изучения: {', '.join(self._courses_attached).removesuffix(',')}"
            f"Завершенные курсы: {', '.join(self._finished_courses).removesuffix(',')}"
        )

    def __lt__(self, other):
        return (
            f"{self.get_name()} имеет больший средний балл"
            if self.get_hw_media() > other.get_hw_media()
            else f"{other.get_name()} имеет больший средний балл"
        )

    def attach_course(self, course_name: str) -> None:
        if self.course_exists(course_name):
            print(f"Студент [ {self.get_name()} {self.get_surname()} ] уже записан на данный курс [ {course_name} ]", end="\n")
            return
        self._courses_attached.append(course_name)

    def finish_course(self, course_name: str) -> None:
        if self.course_exists(course_name):
            self._finished_courses.append(course_name)
            self._courses_attached.remove(course_name)
        else:
            print(f"Ошибкаб нету такого курса [ {course_name} ] в начатых", end="\n")
            return

    def get_hw_media(self) -> float:
        media: float = 0.0
        for course in self._grades:
            media += sum(self._grades.get(course)) / len(self._grades.get(course))
        return media

    def get_course_marks(self, course_name) -> list:
        return self._grades[course_name]

    def course_exists(self, course_name):
        return self._courses_attached.__contains__(course_name)

    def set_lector_mark(self, lector, course_name: str, mark: int) -> None:
        if not self.course_exists(course_name):
            print(f"Студент [ {self.get_name()} {self.get_surname()} ] не подписан на данный курс [ {course_name} ]", end="\n")
            return
        elif not lector.course_exists(course_name):
            print(f"Лектор [ {lector.get_name()} {lector.get_surname()} ] не ведет на данный курс [ {course_name} ]", end="\n")
            return

        lector.set_course_grade(course_name, mark)

    def get_grades(self) -> Dict[str, List[int]]:
        return self._grades

