from abc import ABC
from typing import List, Union

from .MentorModel import Mentor
from .StudentModel import Student


class Reviewer(Mentor, ABC):
    def __init__(self, name: str, surname: str, gender: str):
        super(Reviewer, self).__init__(name, surname, "Reviewer", gender)

    def __str__(self) -> str:
        return f"Имя: {self._name}" f"Фамилия: {self._surname}"

    def rate_hw(self, student: Student, course_name: str, grade: int):
        if (
            isinstance(student, Student)
            and self.course_exists(course_name)
            and student.course_exists(course_name)
        ):
            if course_name in student._grades:
                student._grades[course_name] += [grade]
            else:
                student._grades[course_name] = [grade]
        else:
            print("Ошибка")
