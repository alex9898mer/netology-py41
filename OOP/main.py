from mds import Lector, Student, Reviewer


if __name__ == '__main__':
    print(list({'test': [], 'Python': [], 'Groovy':[]}.keys()).__contains__('test'))
    best_student = Student('Roy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    #
    cool_rev = Reviewer('Some', 'Buddy')
    cool_rev.attach_course('Python')
    cool_rev1 = Lector('Test', 'Buddy')
    cool_rev2 = Lector('Some', 'Buddy')

    cool_rev1.lectures_media = 10.0

    print(cool_rev2 < cool_rev1)
    #
    cool_rev.rate_hw(best_student, 'Python', 10)
    # cool_mentor.rate_hw(best_student, 'Python', 10)
    # cool_mentor.rate_hw(best_student, 'Python', 10)
    #
    print(f"{best_student.grades=}")
