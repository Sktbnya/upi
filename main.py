import random

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

length = 10
min_value = 1
max_value = 100

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
    def __init__(self, subjects, exam_date, teacher_name):
        self.subjects = subjects
        self.exam_date = exam_date
        self.teacher_name = teacher_name


def fill_group(num_students):
    group = []
    for _ in range(num_students):
        first_name = random.choice(["Иван", "Олег", "Никита", "Александр"])
        last_name = random.choice(["Иванов", "Егоров", "Петров", "Смирнов"])
        birth_year = random.randint(2000, 2005)
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        birthday = f"{birth_day:02d}.{birth_month:02d}.{birth_year}"


        num_subjects = random.randint(3, 5)
        subjects = random.choices(["Математика", "Физика", "Английский"], k=num_subjects)
        exam_date = f"{random.randint(1, 28):02d}.{random.randint(1, 12):02d}.2023"
        teacher_name = random.choice(["Иванова А.Н.", "Магомедов П.П.", "Петров Е.В.", "Смирнов Д.А."])

        zachet = Zachet(subjects, exam_date, teacher_name)
        student = Student(first_name, last_name, birthday, zachet)
        group.append(student)

    return group


def print_group(group):
    for student in group:
        print("Фамилия и имя:", student.last_name, student.first_name)
        print("Дата рождения:", student.birthday)
        print("Зачетка:")
        print("  Предметы:", ", ".join(student.zachet.subjects))
        print("  Дата экзамена:", student.zachet.exam_date)
        print("  ФИО преподавателя:", student.zachet.teacher_name)
        print()

num_students = 5

group = fill_group(num_students)
print_group(group)
