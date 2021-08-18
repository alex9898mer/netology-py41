from abc import ABC
from typing import List

from .BaseModel import Base


class Student(Base, ABC):
    def __init__(self, name: str, surname: str, *args):
        super(Student, self).__init__(name, surname, "Student", *args)

    def __str__(self) -> str:
        return (
            f"Имя: {self._name}\n"
            f"Фамилия: {self._surname}\n"
            f"Средняя оценка за домашние задания: {self.get_hw_media()}\n"
            f"Курсы в процессе изучения: {', '.join(self._enrolled_courses).removesuffix(',')}\n"
            f"Завершенные курсы: {', '.join(self._finished_courses).removesuffix(',')}\n"
        )

    def __lt__(self, other):
        return (
            f"{self.get_name()} имеет больший средний балл\n"
            if self.get_hw_media() > other.get_hw_media()
            else f"{other.get_name()} имеет больший средний балл\n"
        )

    def get_hw_media(self) -> float:
        media: List[float] = []
        for course in self._grades:
            media.append(sum(self._grades.get(course)) / len(self._grades.get(course)))
        return float((sum(media) / media.__len__()).__format__(".4"))

    def get_course_marks(self, course_name) -> list:
        return self._grades[course_name]

    def set_lector_mark(self, lector, course_name: str, mark: int) -> None:
        if not self.course_exists(course_name):
            print(
                f"{self.get_role()} [ {self.get_name()} {self.get_surname()} ] не подписан на данный курс [ {course_name} ]",
                end="\n",
            )
            return
        elif not lector.course_exists(course_name):
            print(
                f"{lector.get_role()} [ {lector.get_name()} {lector.get_surname()} ] не ведет данный курс [ {course_name} ]",
                end="\n",
            )
            return

        lector.set_course_grade(course_name, mark)
