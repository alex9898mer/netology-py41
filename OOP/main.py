from typing import List, Union

from models import Student, Reviewer, Lector


def main():
    # Initialize roles
    student1: Student = Student(name="John", surname="Doe")
    student2: Student = Student(name="Luis", surname="Hack")
    reviewer1: Reviewer = Reviewer(name="Ketty", surname="Shoe", gender="female")
    reviewer2: Reviewer = Reviewer(name="Kate", surname="Black", gender="female")
    lector1: Lector = Lector(name="Magnus", surname="Grant")
    lector2: Lector = Lector(name="Matt", surname="White")

    """
        Provision roles
    """
    # Attach courses
    student1.attach_courses(courses="Python")
    student1.attach_courses(courses=["Go", "Java"])

    student2.attach_courses(courses="Python")
    student2.attach_courses(courses=[".Net", "Java"])

    reviewer1.attach_courses(courses="Python")
    reviewer1.attach_courses(courses=["Ruby", "Java"])

    reviewer2.attach_courses(courses="Go")
    reviewer2.attach_courses(courses=["Python", ".Net"])

    lector1.attach_courses(courses="Go")
    lector1.attach_courses(courses=[".Net", "Java"])

    lector2.attach_courses(courses="Ruby")
    lector2.attach_courses(courses=["Java", "Python"])

    # Set student grades
    reviewer1.rate_hw(student=student1, course_name="Python", grade=10)
    reviewer1.rate_hw(student=student1, course_name="Python", grade=9)
    reviewer1.rate_hw(student=student1, course_name="Python", grade=5)
    reviewer1.rate_hw(student=student1, course_name="Java", grade=9)
    reviewer1.rate_hw(student=student1, course_name="Java", grade=9)
    reviewer1.rate_hw(student=student1, course_name="Java", grade=10)

    reviewer1.rate_hw(student=student2, course_name="Python", grade=7)
    reviewer1.rate_hw(student=student2, course_name="Python", grade=8)
    reviewer1.rate_hw(student=student2, course_name="Python", grade=9)
    reviewer1.rate_hw(student=student2, course_name="Java", grade=8)
    reviewer1.rate_hw(student=student2, course_name="Java", grade=9)
    reviewer1.rate_hw(student=student2, course_name="Java", grade=7)

    reviewer2.rate_hw(student=student1, course_name="Python", grade=10)
    reviewer2.rate_hw(student=student1, course_name="Python", grade=9)
    reviewer2.rate_hw(student=student1, course_name="Python", grade=5)
    reviewer2.rate_hw(student=student1, course_name="Go", grade=10)
    reviewer2.rate_hw(student=student1, course_name="Go", grade=9)
    reviewer2.rate_hw(student=student1, course_name="Go", grade=5)

    reviewer2.rate_hw(student=student2, course_name="Python", grade=10)
    reviewer2.rate_hw(student=student2, course_name="Python", grade=9)
    reviewer2.rate_hw(student=student2, course_name="Python", grade=5)
    reviewer2.rate_hw(student=student2, course_name=".Net", grade=10)
    reviewer2.rate_hw(student=student2, course_name=".Net", grade=9)
    reviewer2.rate_hw(student=student2, course_name=".Net", grade=5)

    # Set lector grades
    student1.set_lector_mark(lector=lector1, course_name="Go", mark=10)
    student1.set_lector_mark(lector=lector1, course_name="Go", mark=8)
    student1.set_lector_mark(lector=lector1, course_name="Go", mark=7)
    student1.set_lector_mark(lector=lector1, course_name="Java", mark=7)
    student1.set_lector_mark(lector=lector1, course_name="Java", mark=7)
    student1.set_lector_mark(lector=lector1, course_name="Java", mark=7)

    student2.set_lector_mark(lector=lector1, course_name=".Net", mark=10)
    student2.set_lector_mark(lector=lector1, course_name=".Net", mark=5)
    student2.set_lector_mark(lector=lector1, course_name=".Net", mark=7)
    student2.set_lector_mark(lector=lector1, course_name="Java", mark=7)
    student2.set_lector_mark(lector=lector1, course_name="Java", mark=8)
    student2.set_lector_mark(lector=lector1, course_name="Java", mark=7)

    student1.set_lector_mark(lector=lector2, course_name="Python", mark=9)
    student1.set_lector_mark(lector=lector2, course_name="Python", mark=6)
    student1.set_lector_mark(lector=lector2, course_name="Python", mark=8)
    student1.set_lector_mark(lector=lector2, course_name="Java", mark=8)
    student1.set_lector_mark(lector=lector2, course_name="Java", mark=10)
    student1.set_lector_mark(lector=lector2, course_name="Java", mark=9)

    student2.set_lector_mark(lector=lector2, course_name="Python", mark=7)
    student2.set_lector_mark(lector=lector2, course_name="Python", mark=5)
    student2.set_lector_mark(lector=lector2, course_name="Python", mark=10)
    student2.set_lector_mark(lector=lector2, course_name="Java", mark=9)
    student2.set_lector_mark(lector=lector2, course_name="Java", mark=10)
    student2.set_lector_mark(lector=lector2, course_name="Java", mark=7)

    """
        Comparisons
    """

    print(f"\n{'='*30} Сравнивание двух лекторов между собой {'='*30}\n")
    print(
        f"[ {lector1.get_name()} ] {lector1.get_grades()=} ==> {lector1.get_lectures_media()=}",
        end="\n",
    )
    print(
        f"[ {lector2.get_name()} ] {lector2.get_grades()=} ==> {lector2.get_lectures_media()=}",
        end="\n",
    )
    print(lector1 < lector2, end="\n")

    print(f"\n{'='*30} Сравнивание двух студентов между собой {'='*30}\n")
    print(
        f"[ {student1.get_name()} ] {student1.get_grades()=} ==> {student1.get_hw_media()=}",
        end="\n",
    )
    print(
        f"[ {student2.get_name()} ] {student2.get_grades()=} ==> {student2.get_hw_media()=}",
        end="\n",
    )
    print(student1 < student2)

    """
        Task 4
    """

    task4("Python", [student1, student2])
    task4("Python", [lector1, lector2])


def task4(course_name: str, recipients: List[Union[Student, Lector]]):
    lecture_media: List[float] = []
    for recipient in recipients:
        if recipient.course_exists(course_name):
            lecture_media.append(
                sum(recipient.get_grades().get(course_name))
                / recipient.get_grades().get(course_name).__len__()
            )
    print(
        f"Средняя оценка по всем {recipients[0].get_role()} записанных на курс [ {course_name} ] "
        f"==> {float((sum(lecture_media) / lecture_media.__len__()).__format__('.4'))}",
        end="\n",
    )


if __name__ == "__main__":
    main()
