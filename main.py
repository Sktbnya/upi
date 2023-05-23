import random

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


def student(self, first_name, last_name, birthday, zachet):
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = birthday
    self.zachet = zachet

def zachet(self, subjects, exam_date, teacher_name):
        self.subjects = subjects
        self.exam_date = exam_date
        self.teacher_name = teacher_name

def fill_group(num_students):
    group = []
    for _ in range(num_students):
        first_name = random.choice(["Иван", "Анна", "Петр", "Мария"])
        last_name = random.choice(["Иванов", "Сидоров", "Петров", "Смирнов"])
        birth_year = random.randint(1990, 2000)
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        birthday = f"{birth_year}-{birth_month:02d}-{birth_day:02d}"

        num_subjects = random.randint(3, 5)
        subjects = random.sample(["Математика", "Физика", "История", "Литература", "Английский"], num_subjects)
        exam_date = f"2023-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        teacher_name = random.choice(["Иванова А.Н.", "Петров П.П.", "Сидорова Е.В.", "Смирнов Д.А."])

        zachet = RecordBook(subjects, exam_date, teacher_name)
        student = Student(first_name, last_name, birthdayday, zachet)
        group.append(student)