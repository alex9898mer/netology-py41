from abc import ABC

from .BaseModel import Base
from .StudentModel import Student


class Mentor(Base, ABC):
    def __init__(self, name: str, surname: str, status: str, *args):
        super(Mentor, self).__init__(
            name, surname, status if status else "Mentor", *args
        )

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

    def get_lectures_media(self) -> float:
        print(f"{self.get_role()} не может иметь оценок за лекции")
        return 0
