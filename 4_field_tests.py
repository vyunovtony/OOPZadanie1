from collections import defaultdict
from statistics import mean
import functools

@functools.total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = defaultdict(list)

    def rate(self, lecturer: 'Lecturer', mark: int, lesson: str) -> None:
        """Метод для выставления оценки лектору"""
        if lesson in self.courses_in_progress and lesson in lecturer.courses_attached:
            """Проверка закреплен ли лектор за курсом, на который записан студент"""
            lecturer.grades[lesson].append(mark)

    def __str__(self) -> str:
        average_grade = mean([sum(grades) / len(grades) for grades in self.grades.values()])
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {average_grade}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        """
    
    def __eq__(self, student: 'Student') -> bool:
        marks1 = self.grades.values()
        marks2 = student.grades.values()
        return (sum(marks1) / len(marks1)) == (sum(marks2) / len(marks2))
    
    def __lt__(self, student: 'Student') -> bool:
        marks1 = self.grades.values()
        marks2 = student.grades.values()
        return (sum(marks1) / len(marks1)) < (sum(marks2) / len(marks2))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@functools.total_ordering
class Lecturer(Mentor):
    """Класс Лектор"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = defaultdict(list)

    def __str__(self) -> str:
        average_grade = mean([sum(grades) / len(grades) for grades in self.grades.values()])
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {average_grade}
        """
    
    def __eq__(self, lecturer: 'Lecturer') -> bool:
        average_grade1 = mean([sum(grades) / len(grades) for grades in self.grades.values()])
        average_grade2 = mean([sum(grades) / len(grades) for grades in lecturer.grades.values()])
        return average_grade1 == average_grade2
    
    def __lt__(self, lecturer: 'Lecturer') -> bool:
        average_grade1 = mean([sum(grades) / len(grades) for grades in self.grades.values()])
        average_grade2 = mean([sum(grades) / len(grades) for grades in lecturer.grades.values()])
        return average_grade1 < average_grade2


class Reviewer(Mentor):
    """Класс Эксперт"""

    def rate(self, student: Student, mark: int, lesson: str) -> None:
        """Метод для выставления оценки студенту"""
        student.grades[lesson].append(mark)

    def __str__(self) -> str:
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        """
    

def calculating_the_average_student_grade(students: list[Student], course_name: str) -> dict[Student: float]:
    average_grades = dict()
    for student in students:
        grades = student.grades.get(course_name)
        if grades:
            average_grades[student] = sum(grades) / len(grades)
    return average_grades
            

def calculating_the_average_rating_of_lecturers(lecturers: list[Lecturer], course_name: str) -> dict[Lecturer: float]:
    average_grades = dict()
    for lecturer in lecturers:
        grades = lecturer.grades.get(course_name)
        if grades:
            average_grades[lecturer] = sum(grades) / len(grades)
    return average_grades


student1 = Student("Alice", "Smith", "female")
student2 = Student("Bob", "Johnson", "male")

lecturer1 = Lecturer("Professor", "Green")
lecturer2 = Lecturer("Dr. Brown", "Lee")

reviewer1 = Reviewer("Mr.", "White")
reviewer2 = Reviewer("Ms.", "Black")


student1.courses_in_progress.append('Math')
student1.courses_in_progress.append('Physics')
student2.courses_in_progress.append('Physics')
student2.courses_in_progress.append('Math')
student1.finished_courses.append('English')
student2.finished_courses.append('English')
lecturer1.courses_attached.append('Math')
lecturer1.courses_attached.append('Physics')
lecturer2.courses_attached.append('Math')
lecturer2.courses_attached.append('Physics')

# Вызовем метод rate у эксперта для выставления оценок студентам
reviewer1.rate(student1, 5, "Math")
reviewer1.rate(student1, 4, "Math")
reviewer2.rate(student2, 4, "Physics")
reviewer2.rate(student2, 3, "Physics")

# Вызовем метод rate у студентов для выставления оценок лекторам
student1.rate(lecturer1, 4, "Math")
student1.rate(lecturer1, 3, "Math")
student2.rate(lecturer2, 5, "Physics")
student2.rate(lecturer2, 4, "Physics")

# Выведем информацию о студентах
print(student1)
print(student2)

# Выведем информацию о лекторах
print(lecturer1)
print(lecturer2)

# Выведем информацию об экспертах
print(reviewer1)
print(reviewer2)