from typing import List, Union
from abc import ABC

from .MentorModel import Mentor
from .StudentModel import Student


class Lector(Mentor, ABC):
    """
    Model which represents Lector object
    """

    def __init__(self, name, surname, course_name=None):
        super(Lector, self).__init__(name, surname)
        self.attach_course(course_name)
        self.lectures_media: float = 0.0

    def __str__(self) -> str:
        """
            Method used to represent model as string object
        :return: String representation of the lector model
        """
        return (
            f"Имя: {self._name}"
            f"Фамилия: {self._surname}"
            f"Средняя оценка за лекции: {self.lectures_media} \n"
        )

    def __lt__(self, other) -> str:
        """
            Method used for comparison with other Lector object by lectures media grade
        :param other: Lector model object used for comparison
        :return: String result of the comparison between two Lector models
        """
        return (
            f"{self.get_name()} {self.get_surname()} имеет больший средний балл за лекции \n"
            if self.lectures_media > other.lectures_media
            else f"{other.get_name()} {other.get_surname()} имеет больший средний балл за лекции \n"
        )

    def get_student_marks(
        self, student: Student, course_name: str
    ) -> Union[list, None]:
        """
            Method used to get student marks for the specific course
        :param student: Student object which marks should be got
        :param course_name: Course name to get marks
        :return: Student marks if specific course is found, else returns None
        """

        if course_name not in self._courses_attached:
            print(f"Данный лектор не ведет этот курс [ {course_name} ]", end="\n")
            return
        elif not student._courses_attached.__contains__(course_name):
            print(
                f"Студент [ {student._name} {student._surname} ] не имеет данного курса в начатых",
                end="\n",
            )
            return
        elif not student._grades.keys().__contains__(course_name):
            print(
                f"Студент [ {student._name} {student._surname} ] не имеет оценок по данному курсу",
                end="\n",
            )
            return

        return student.get_course_marks(course_name)

    def course_exists(self, course_name: str) -> bool:
        """
            Method used to find if lector is enrolled on the course
        :param course_name: Course to search for
        :return: Course exists or not as enrolled
        """
        return self._courses_attached.__contains__(course_name)

    def recalculate_lectures_media(self) -> None:
        lectures_media: float = 0.0
        if not list(self._grades.keys()):
            return

        for course in self._grades:
            lectures_media += (
                    sum(self._grades.get(course)) / self._grades.get(course).__len__()
            )
        self.lectures_media = lectures_media

    def set_course_grade(self, course_name: str, mark: int) -> None:
        """
            Method used to set grade from student for specific course
        :param course_name: Course to set mark for
        :param mark: Mark to set for course
        :return:
        """

        if not self.course_exists(course_name):
            self._grades.update({ course_name: [mark]})
        else:
            self._grades.get(course_name).append(mark)

        # Recalculate lectors grades media on every new added grade
        self.recalculate_lectures_media()

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_attached_courses(self) -> List[str]:
        return self._courses_attached

