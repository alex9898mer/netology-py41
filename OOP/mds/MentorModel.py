from abc import ABC
from typing import TYPE_CHECKING

from .BaseModel import Base
from .StudentModel import Student
from .ReviewerModel import Reviewer

if TYPE_CHECKING:
    pass


class Mentor(Base, ABC):
    def __init__(self, name, surname):
        super(Mentor, self).__init__(name, surname)

    def attach_course(self, course_name):
        if course_name:
            self.courses_attached.append(course_name)

    def rate_hw(self, student, course, grade):

        if (
            isinstance(student, Student)
            and isinstance(self, Reviewer)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("Ошибка")
