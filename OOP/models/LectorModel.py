from typing import List, Union
from abc import ABC

from .MentorModel import Mentor
from .StudentModel import Student


class Lector(Mentor, ABC):
    """
    Model which represents Lector object
    """

    def __init__(self, name: str, surname: str, *args, course_name: str = None):
        super(Lector, self).__init__(name, surname, "Lector", *args)
        self.attach_courses(course_name)
        self._lectures_media: float = 0.0

    def __str__(self) -> str:
        """
            Method used to represent model as string object
        :return: String representation of the lector model
        """
        return (
            f"Имя: {self._name}\n"
            f"Фамилия: {self._surname}\n"
            f"Средняя оценка за лекции: {self._lectures_media} \n"
        )

    def __lt__(self, other) -> str:
        """
            Method used for comparison with other Lector object by lectures media grade
        :param other: Lector model object used for comparison
        :return: String result of the comparison between two Lector models
        """
        return (
            f"{self.get_name()} {self.get_surname()} имеет больший средний балл за лекции \n"
            if self._lectures_media > other._lectures_media
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

        if course_name not in self._enrolled_courses:
            print(f"Данный лектор не ведет этот курс [ {course_name} ]", end="\n")
            return
        elif not student._enrolled_courses.__contains__(course_name):
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

    def recalculate_lectures_media(self) -> None:
        lectures_media: List[float] = []
        if not list(self._grades.keys()):
            return

        for course in self._grades:
            lectures_media.append(
                sum(self._grades.get(course)) / self._grades.get(course).__len__()
            )
        self._lectures_media = float(
            (sum(lectures_media) / lectures_media.__len__()).__format__(".4")
        )

    def set_course_grade(self, course_name: str, mark: int) -> None:
        """
            Method used to set grade from student for specific course
        :param course_name: Course to set mark for
        :param mark: Mark to set for course
        :return:
        """

        if self.course_exists(course_name) and list(self._grades.keys()).__contains__(
            course_name
        ):
            self._grades.get(course_name).append(mark)
        else:
            self._grades.update({course_name: [mark]})

        # Recalculate lectors grades media on every new added grade
        self.recalculate_lectures_media()

    def rate_hw(self, student: Student, course_name: str, grade: int):
        print(
            f"{self.get_name()} {self.get_surname()} не может выставлять оценки студентам из-за своего статуса {self.get_role()}"
        )

    def get_lectures_media(self) -> float:
        return self._lectures_media
