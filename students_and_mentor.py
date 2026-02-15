class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Method for adding a course to the list of completed ones
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Method for grading a lecturer
    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                course in self.courses_in_progress and
                course in lecturer.courses_attached and 1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    # Overriding the __str__ method
    def __str__(self):
        in_progress = (", ".join(self.courses_in_progress)
                       if self.courses_in_progress else "Курсов нет")
        finished = (', '.join(self.finished_courses)
                    if self.finished_courses else "Курсов нет")
        avg = self.average_grade()
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg}\n"
            f"Курсы в процессе изучения: {in_progress}\n"
            f"Завершенные курсы: {finished}"
        )

    # Overriding the comparison method ==
    def __eq__(self, student):
        if isinstance(student, Student):
            return self.average_grade() == student.average_grade()
        else:
            return 'Ошибка'

    # Overriding the comparison method <
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() < student.average_grade()
        else:
            return 'Ошибка'

    # Overriding the comparison method >
    def __gt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() > student.average_grade()
        else:
            return 'Ошибка'

    # Method for calculating the average grade for homework assignments
    def average_grade(self):
        if self.grades:
            sum_grades = 0
            total_grades = 0
            for course in self.grades.values():
                sum_grades += sum(course)
                total_grades += len(course)
            return round(sum_grades / total_grades, 1)
        else:
            return 0


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # Overriding the __str__ method
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Overriding the __str__ method
    def __str__(self):
        parent = super().__str__()
        return parent + f"\nСредняя оценка за лекции: {self.average_grade()}"

    # Method for calculating the average grade for lectures
    def average_grade(self):
        if self.grades:
            sum_grades = 0
            total_grades = 0
            for course in self.grades.values():
                sum_grades += sum(course)
                total_grades += len(course)
            return round(sum_grades / total_grades, 1)
        else:
            return 0

    # Overriding the comparison method ==
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() == lecturer.average_grade()
        else:
            return 'Ошибка'

    # Overriding the comparison method <
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() < lecturer.average_grade()
        else:
            return 'Ошибка'

    # Overriding the comparison method >
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() > lecturer.average_grade()
        else:
            return 'Ошибка'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Method for grading a student.
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress and 1 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


def average_grade_homeworks(students_list, course):
    """A function to calculate the average homework 
    grade of all students (listed) in a given course."""
    total_grades = 0
    sum_grades = 0
    for student in students_list:
        if isinstance(student, Student) and course in student.grades:
            sum_grades += sum(student.grades[course])
            total_grades += len(student.grades[course])
    if total_grades:
        return round(sum_grades / total_grades, 1)
    else:
        return 0


def average_grade_lecturer(lecturer_list, course):
    """Function for calculating the average lecture 
    grade of all lecturers (listed) in a given course."""
    total_grades = 0
    sum_grades = 0
    for lecturer in lecturer_list:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            total_grades += len(lecturer.grades[course])
    if total_grades:
        return round(sum_grades / total_grades, 1)
    else:
        return 0


student_1 = Student('Peter', 'Parker', 'male')
student_1.courses_in_progress = ['Python', 'Git']
student_2 = Student('Mary', 'Jane', 'female')
student_2.courses_in_progress = ['Python', 'Java']

lecturer_1 = Lecturer('Kevin', 'Eastman')
lecturer_1.courses_attached = ['Python', 'Git']
lecturer_2 = Lecturer('Peter', 'Laird')
lecturer_2.courses_attached = ['Python', 'Java']

reviewer_1 = Reviewer('Gandalf', 'Gray')
reviewer_1.courses_attached = ['Git', 'Python']
reviewer_2 = Reviewer('Radagast', 'Brown')
reviewer_2.courses_attached = ['Java', 'Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)

student_1.add_courses('Введение в программирование')
student_1.rate_lecture(lecturer_1, 'Python', 6)
student_1.rate_lecture(lecturer_1, 'Git', 7)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Java', 8)

print(f"\nМетод __str__ для класса Student: \n{student_1}")
print(f"\nМетод __str__ для класса Lecturer: \n{lecturer_1}")
print(f"\nМетод __str__ для класса Reviewer: \n{reviewer_1}")

print()

print(f"s1 = {student_1.average_grade()} s2 = {student_2.average_grade()}")
print(f"Результат сравнения студентов (s1 < s2): {student_1 < student_2}")
print(f"Результат сравнения студентов (s1 > s2): {student_1 > student_2}")
print(f"Результат сравнения студентов (s1 == s2): {student_1 == student_2}")
student_1.grades['Python'] = [6, 9, 9]
student_1.grades['Git'] = [5, 5, 6]
student_2.grades['Python'] = [6, 9, 9, 6]
student_2.grades['Java'] = [5, 5]
print(f"s1 = {student_1.average_grade()} s2 = {student_2.average_grade()}")
print(f"Результат сравнения студентов (s1 == s2): {student_1 == student_2}")

print()

print(f"l1 = {lecturer_1.average_grade()} l2 = {lecturer_2.average_grade()}")
print(f"Результат сравнения лекторов (l1 < l2): {lecturer_1 < lecturer_2}")
print(f"Результат сравнения лекторов (l1 > l2): {lecturer_1 > lecturer_2}")
print(f"Результат сравнения лекторов (l1 == l2): {lecturer_1 == lecturer_2}")
lecturer_2.grades['Java'] = [6]
print(f"l1 = {lecturer_1.average_grade()} l2 = {lecturer_2.average_grade()}")
print(f"Результат сравнения лекторов (l1 == l2): {lecturer_1 == lecturer_2}")

print()

student_avg = average_grade_homeworks([student_1, student_2], 'Python')
lecturer_avg = average_grade_lecturer([lecturer_1, lecturer_2], 'Python')
print(f"Средняя оценка всех студентов по курсу Python: {student_avg}")
print(f"Средняя оценка всех лекторов по курсу Python: {lecturer_avg}")
