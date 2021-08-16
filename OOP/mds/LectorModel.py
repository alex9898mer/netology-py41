from typing import Union
from abc import ABC

from .MentorModel import Mentor
from .StudentModel import Student


class Lector(Mentor, ABC):
    def __init__(self, name, surname, course_name=None):
        super(Lector, self).__init__(name, surname)
        self.attach_course(course_name)
        self.lectures_media: float = 9.5

    ################
    # Задание 3
    ################
    def __str__(self) -> str:
        return (
            f"Имя: {self.name}"
            f"Фамилия: {self.surname}"
            f"Средняя оценка за лекции: {self.get_lectures_media()}"
        )

    def __lt__(self, other) -> str:
        return (
            f"{self.name} имеет больший средний балл"
            if self.get_lectures_media() > other.get_lectures_media()
            else f"{other.name} имеет больший средний балл"
        )

    def get_student_marks(self, student: Student, course_name: str) -> Union[list, str]:
        if course_name not in self.courses_attached:
            return f"Данный лектор не ведет этот курс [ {course_name} ]"
        elif not student.courses_in_progress.__contains__(course_name):
            return f"Студент [ {student.name} {student.surname} ] не имеет данного курса в начатых"
        elif not student.grades.keys().__contains__(course_name):
            return f"Студент [ {student.name} {student.surname} ] не имеет оценок по данному курсу"

        return student.get_course_marks(course_name)

    def course_exists(self, course_name):
        return self.courses_attached.__contains__(course_name)

    def get_lectures_media(self) -> float:
        return self.lectures_media

    def set_course_grade(self, mark):
        pass
