from collections import defaultdict


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = defaultdict(list)

    def rate(self, lecturer: "Lecturer", mark: int, lesson: str) -> None:
        """Метод для выставления оценки лектору"""
        if lesson in self.courses_in_progress and lesson in lecturer.courses_attached:
            """Проверка закреплен ли лектор за курсом, на который записан студент"""
            lecturer.grades[lesson].append(mark)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Класс Лектор"""

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = defaultdict(list)


class Reviewer(Mentor):
    """Класс Эксперт"""

    def rate(self, student: Student, mark: int, lesson: str) -> None:
        """Метод для выставления оценки студенту"""
        student.grades[lesson].append(mark)
