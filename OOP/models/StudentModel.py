from typing import List, TYPE_CHECKING
from abc import ABC

from .BaseModel import Base

if TYPE_CHECKING:
    from .LectorModel import Lector


class Student(Base, ABC):
    def __init__(self, name, surname, gender):
        super(Student, self).__init__(name, surname, gender)
        self.finished_courses: List[str] = []

    def __str__(self) -> str:
        return (
            f"Имя: {self.name}"
            f"Фамилия: {self.surname}"
            f"Средняя оценка за домашние задания: {self.get_hw_media()}"
            f"Курсы в процессе изучения: {', '.join(self.courses_attached)}"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        return (
            f"{self.name} имеет больший средний балл"
            if self.get_hw_media() > other.get_hw_media()
            else f"{other.name} имеет больший средний балл"
        )

    def attach_course(self, course_name):
        self.courses_attached.append(course_name)

    def finish_course(self, course_name):
        if course_name in self.courses_attached:
            self.finished_courses.append(course_name)
            self.courses_attached.remove(course_name)
        else:
            print("Ошибкаб нету такого курса в начатых")

    def get_hw_media(self) -> float:
        media: float = 0.0
        for course in self.grades:
            media += sum(self.grades.get(course)) / len(self.grades.get(course))
        return media

    def get_course_marks(self, course_name) -> list:
        return self.grades[course_name]

    def _course_exists(self, course_name):
        return self.courses_attached.__contains__(course_name)

    def set_lector_mark(self, lector: Lector, course_name: str, mark: int):
        if not self._course_exists(course_name):
            return f"Студент [ {self.name} {self.surname} ] не подписан на данный курс [ {course_name} ]"
        elif not lector._course_exists(course_name):
            return f"Лектор [ {lector.name} {lector.surname} ] не ведет на данный курс [ {course_name} ]"

        lector.set_course_grade(course_name, mark)
