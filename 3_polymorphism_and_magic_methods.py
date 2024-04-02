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
        Курсы в процессе изучения: {self.courses_in_progress}
        Завершенные курсы: {self.finished_courses}
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