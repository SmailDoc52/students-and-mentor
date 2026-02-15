class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод для добавления курса в список завершенных
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Метод для выставления оценки лектору
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

    # Переопределяем метод __str__
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

    # Переопределяем метод сравнения ==
    def __eq__(self, student):
        if isinstance(student, Student):
            return self.average_grade() == student.average_grade()
        else:
            return 'Ошибка'

    # Переопределяем метод сравнения <
    def __lt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() < student.average_grade()
        else:
            return 'Ошибка'

    # Переопределяем метод сравнения >
    def __gt__(self, student):
        if isinstance(student, Student):
            return self.average_grade() > student.average_grade()
        else:
            return 'Ошибка'

    # Метод для подсчета средней оценки за домашние задания
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

    # Переопределяем метод __str__
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}"
        )


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Переопределяем метод __str__
    def __str__(self):
        parent = super().__str__()
        return parent + f"\nСредняя оценка за лекции: {self.average_grade()}"

    # Метод для подсчета средней оценки за лекции
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

    # Переопределяем метод сравнения ==
    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() == lecturer.average_grade()
        else:
            return 'Ошибка'

    # Переопределяем метод сравнения <
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() < lecturer.average_grade()
        else:
            return 'Ошибка'

    # Переопределяем метод сравнения >
    def __gt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self.average_grade() > lecturer.average_grade()
        else:
            return 'Ошибка'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод для выставления оценки студенту
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
