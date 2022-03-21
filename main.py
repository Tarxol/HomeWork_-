class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        average_List = (sum(self.grades.values(),[]))
        return (sum(average_List) / len(average_List))

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return first_student.average_grade() < other.average_grade()

    def __str__(self):
        return f"\nИмя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за домашние задания: {self.average_grade()}" \
               f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}" \
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        average_List = (sum(self.grades.values(),[]))
        return (sum(average_List) / len(average_List))

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        return f"\nИмя: {self.name}" \
               f"\nФамилия: {self.surname}" \
               f"\nСредняя оценка за лекции: {self.average_grade()}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f"\nИмя: {self.name}" \
               f"\nФамилия: {self.surname}" \

first_student = Student('Ruoy', 'Eman', 'boy')
first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['English']

second_student = Student('Anna', 'Fox', 'girl')
second_student.courses_in_progress += ['Python']

first_reviewer = Reviewer('Alex', 'King')
first_reviewer.courses_attached += ['Python']

second_reviewer = Reviewer('Elena', 'Queen')
second_reviewer.courses_attached += ['Git']

first_lecturer = Lecturer('Big', 'Boss')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Peter', 'Hines')
second_lecturer.courses_attached += ['Git']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 5)

first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 10)

second_reviewer.rate_hw(first_student, 'Git', 8)
second_reviewer.rate_hw(first_student, 'Git', 2)

first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(second_lecturer, 'Git', 10)
first_student.rate_lecturer(second_lecturer, 'Git', 2)
second_student.rate_lecturer(first_lecturer, 'Python', 8)

students_list = [first_student, second_student]
lecturers_list = [first_lecturer, second_lecturer]

def average_grade_students_course(students_list , course):
    grades_students_course = []
    for student in students_list:
        if course in student.courses_in_progress:
            grades_students_course += student.grades[course]
    return f'Средняя оценка студентов за Д/З на курсе {course} = {sum(grades_students_course) / len(grades_students_course)}'

def average_grade_lecturer_course(lectorers_list, course):
    grades_lecturer_course = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            grades_lecturer_course += lecturer.grades[course]
    return f'Средняя оценка лекторов на курсе {course} = {sum(grades_lecturer_course) / len(grades_lecturer_course)}'



print(first_student)
print(second_student)
print(first_reviewer)
print(second_reviewer)
print(first_lecturer)
print(second_lecturer)
print(first_student < second_student)
print(first_lecturer > second_lecturer)
print(average_grade_students_course(students_list, 'Python'))
print(average_grade_lecturer_course(lecturers_list, 'Git'))
