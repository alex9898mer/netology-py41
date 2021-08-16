from abc import ABC

from .MentorModel import Mentor


class Reviewer(Mentor, ABC):
    def __init__(self, name, surname):
        super(Reviewer, self).__init__(name, surname)

    def __str__(self) -> str:
        return f"Имя: {self.name}" f"Фамилия: {self.surname}"
