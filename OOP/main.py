from models import Student, Reviewer, Lector


def test1():
    reviewer = Reviewer("Some", "Buddy")
    student = Student("Roy", "Eman", "your_gender")
    student.attach_courses("Python")
    #
    reviewer.attach_courses("Python")
    reviewer1 = Lector("Test", "Buddy")
    reviewer2 = Lector("Some", "Buddy")

    reviewer1.lectures_media = 10.0

    print(reviewer2 < reviewer1)

    reviewer.rate_hw(student, "Python", 10)

    print(f"{student.get_grades()=}")

    print(reviewer.get_attached_courses(), reviewer1.get_attached_courses(), sep="\n")


def test2():
    # Initialize roles
    student: Student = Student(name="John", surname="Doe")
    reviewer: Reviewer = Reviewer(name="Ketty", surname="Shoe", gender="female")
    lector1: Lector = Lector(name="Magnus", surname="Grant")
    lector2: Lector = Lector(name="Matt", surname="White")
    # Fill roles
    """
        Provision roles
    """
    # Attach courses
    student.attach_courses("Python")
    reviewer.attach_courses("Python")
    lector1.attach_courses(["Go", "Python"])
    lector2.attach_courses(["Java", "Python"])

    # Set grades
    reviewer.rate_hw(student=student, course_name="Python", grade=10)
    reviewer.rate_hw(student=student, course_name="Python", grade=9)
    reviewer.rate_hw(student=student, course_name="Python", grade=5)

    print(f"{student.get_grades()=}")
    """
        Test roles
    """
    print(f"\n{'='*20} Testing enrollment for already started course {'='*20}\n")
    student.attach_courses("Python")
    print(
        f"\n{'='*20} Finished Testing enrollment for already started course {'='*20}\n"
    )


if __name__ == "__main__":
    test2()
