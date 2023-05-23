import random
import datetime

# Часть 1
def fill_array(length, min_value, max_value):
    array = []
    for _ in range(length):
        value = random.randint(min_value, max_value)
        array.append(value)
    return array


def print_array(array):
    for value in array:
        print(value, end=' ')
    print()

length = int(input("Введите длину массива: "))
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))

my_array = fill_array(length, min_value, max_value)
print_array(my_array)

# Часть 2
class Student:
    def __init__(self, first_name, last_name, birthday, zachet):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.zachet = zachet


class Zachet:
    def __init__(self):
        self.subjects = {}

    def add_subject(self, subject, exam_date, teacher_name):
        self.subjects[subject] = {'exam_date': exam_date, 'teacher_name': teacher_name}

    def get_subjects(self):
        return self.subjects.keys()

    def get_exam_date(self, subject):
        return self.subjects[subject]['exam_date']

    def get_teacher_name(self, subject):
        return self.subjects[subject]['teacher_name']



def fill_group(num_students):
    group = []
    for _ in range(num_students):
        first_name = input("Введите имя студента: ")
        last_name = input("Введите фамилию студента: ")
        birth_day = int(input("Введите день рождения студента: "))
        birth_month = int(input("Введите месяц рождения студента: "))
        birth_year = int(input("Введите год рождения студента: "))
        birthday = f"{birth_day:02d}.{birth_month:02d}.{birth_year}"

        num_subjects = int(input("Введите количество предметов студента: "))
        zachet = Zachet()
        for _ in range(num_subjects):
            subject = input("Введите название предмета: ")
            exam_day = int(input("Введите день экзамена: "))
            exam_month = int(input("Введите месяц экзамена: "))
            exam_date = f"{exam_day:02d}.{exam_month:02d}.2023"
            teacher_name = input("Введите ФИО преподавателя: ")
            zachet.add_subject(subject, exam_date, teacher_name)

        student = Student(first_name, last_name, birthday, zachet)
        group.append(student)

    return group



def print_group(group):
    for student in group:
        print("Фамилия и имя:", student.last_name, student.first_name)
        print("Дата рождения:", student.birthday)
        print("Зачетка:")
        for subject in student.zachet.get_subjects():
            print("  Предмет:", subject)
            print("  Дата экзамена:", student.zachet.get_exam_date(subject))
            print("  ФИО преподавателя:", student.zachet.get_teacher_name(subject))
        print()

num_students = int(input("Введите количество студентов в группе: "))

group = fill_group(num_students)
print_group(group)


def find_youngest_student(group):
    current_year = datetime.datetime.now().year
    youngest_student = None
    youngest_age = float('inf')

    for student in group:
        birth_year = int(student.birthday.split('.')[-1])
        age = current_year - birth_year
        if age < youngest_age:
            youngest_age = age
            youngest_student = student

    return youngest_student


def find_oldest_student(group):
    current_year = datetime.datetime.now().year
    oldest_student = None
    oldest_age = 0

    for student in group:
        birth_year = int(student.birthday.split('.')[-1])
        age = current_year - birth_year
        if age > oldest_age:
            oldest_age = age
            oldest_student = student

    return oldest_student


num_students = int(input("Введите количество студентов в группе: "))

group = fill_group(num_students)
print_group(group)

youngest_student = find_youngest_student(group)
oldest_student = find_oldest_student(group)

print("Самый младший студент:")
print("ФИО:", youngest_student.last_name, youngest_student.first_name)
print("Дата рождения:", youngest_student.birthday)

print("Самый старший студент:")
print("ФИО:", oldest_student.last_name, oldest_student.first_name)
print("Дата рождения:", oldest_student.birthday)

