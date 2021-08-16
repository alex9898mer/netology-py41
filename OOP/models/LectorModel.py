from typing import Union
from abc import ABC

from .MentorModel import Mentor
from .StudentModel import Student


class Lector(Mentor, ABC):
    def __init__(self, name, surname, course_name=None):
        super(Lector, self).__init__(name, surname)
        self.attach_course(course_name)
        self.lectures_media: float = 0.0

    ################
    # Задание 3
    ################
    def __str__(self) -> str:
        return (
            f"Имя: {self.name}"
            f"Фамилия: {self.surname}"
            f"Средняя оценка за лекции: {self.lectures_media}"
        )

    def __lt__(self, other) -> str:
        return (
            f"{self.name} имеет больший средний балл"
            if self.lectures_media > other.lectures_media
            else f"{other.name} имеет больший средний балл"
        )

    def get_student_marks(self, student: Student, course_name: str) -> Union[list, str]:
        if course_name not in self.courses_attached:
            return f"Данный лектор не ведет этот курс [ {course_name} ]"
        elif not student.courses_attached.__contains__(course_name):
            return f"Студент [ {student.name} {student.surname} ] не имеет данного курса в начатых"
        elif not student.grades.keys().__contains__(course_name):
            return f"Студент [ {student.name} {student.surname} ] не имеет оценок по данному курсу"

        return student.get_course_marks(course_name)

    def _course_exists(self, course_name):
        return self.courses_attached.__contains__(course_name)

    def recalculate_lectures_media(self):
        lectures_media: float = 0.0
        if not list(self.grades.keys()):
            return lectures_media

        for course in self.grades:
            lectures_media += sum(self.grades.get(course)) / self.grades.get(course).__len__()
        self.lectures_media = lectures_media

    def set_course_grade(self, course_name: str, mark: int):
        if not self._course_exists(course_name):
            self.grades.update({course_name: [mark]})
        else:
            self.grades.get(course_name).append(mark)

        # Recalculate lectors grades media on every new added grade
        self.recalculate_lectures_media()
