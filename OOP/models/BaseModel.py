from typing import List, Dict, Union


class Base:
    def __init__(self, name: str, surname: str, status: str, gender: str = "male"):
        self._name: str = name
        self._surname: str = surname
        self._gender: str = gender
        self._role: str = status
        self._enrolled_courses: List[str] = []
        self._finished_courses: List[str] = []
        self._grades: Dict[str, List[int]] = {}

    def course_exists(self, course_name: str) -> bool:
        """
            Method used to find if lector is enrolled on the course
        :param course_name: Course to search for
        :return: Course exists or not as enrolled
        """
        return self._enrolled_courses.__contains__(course_name.lower().capitalize())

    def __str__(self) -> str:
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def attach_courses(self, course: Union[str, List[str]]) -> None:
        if isinstance(course, List):
            existing_courses: List[str] = []
            for course_name in course:
                if self.course_exists(course_name):
                    existing_courses.append(course_name.lower().capitalize())
                    course.remove(course_name.lower().capitalize())
            if existing_courses:
                print(
                    f"{self.get_name()} {self.get_surname()} уже записан на данные курсы {existing_courses}",
                    end="\n",
                )
            self._enrolled_courses.extend(course)
        elif isinstance(course, str):
            if self.course_exists(course):
                print(
                    f"{self.get_role()} {self.get_name()} {self.get_surname()} уже записан на данный курс [ {course} ]",
                    end="\n",
                )
            self._enrolled_courses.append(course.lower().capitalize())

    def finish_course(self, course_name: str) -> None:
        if self.course_exists(course_name):
            self._finished_courses.append(course_name.lower().capitalize())
            self._enrolled_courses.remove(course_name.lower().capitalize())
        else:
            print(f"Ошибкаб нету такого курса [ {course_name} ] в начатых", end="\n")
            return

    def get_grades(self) -> Dict[str, List[int]]:
        return self._grades

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_role(self) -> str:
        return self._role

    def get_attached_courses(self) -> List[str]:
        return self._enrolled_courses
