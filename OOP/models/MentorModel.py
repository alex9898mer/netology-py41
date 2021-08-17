from abc import ABC
from typing import TYPE_CHECKING

from .BaseModel import Base

from .StudentModel import Student
# from .ReviewerModel import Reviewer
if TYPE_CHECKING:
    pass


class Mentor(Base, ABC):
    def __init__(self, name, surname):
        super(Mentor, self).__init__(name, surname)

    def attach_course(self, course_name):
        if course_name:
            self._courses_attached.append(course_name)

    def rate_hw(self, student: Student, course_name: str, grade: int):

        if (
            isinstance(student, Student)
            # and isinstance(cls, Reviewer)
            and self.course_exists(course_name)
            and student.course_exists(course_name)
        ):
            if course_name in student._grades:
                student._grades[course_name] += [grade]
            else:
                student._grades[course_name] = [grade]
        else:
            print("Ошибка")

    def course_exists(self, course_name: str) -> bool:
        return self._courses_attached.__contains__(course_name)
