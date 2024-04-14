# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self . name + ' ' + self . surname

class Parent(Person):
    def __init__(self, name, surname):
        self.person = Person(name, surname)

class Student(Person):
    def __init__(self, name, surname, parents: list [Parent]):
        self.person = Person(name, surname)
        self.parents = parents

class Subject:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, surname, subject):
        self.person = Person(name, surname)
        self.subject = subject

class Class:
    def __init__(self, name, teachers:list [Teacher], students: list[Student]):
        self.name = name
        self.teachers = teachers
        self.students = students

    def print_all_student(self):
        print('Список учеников {} класса'.format(self.name))
        for item in self.students:
            print(item.person.get_full_name())
    
    def print_all_techer(self):
        print('Список преподаватлей {}'.format(self.name))
        for teacher in self.teachers:
            print(teacher.person.get_full_name())


class School:
    def __init__(self, name, classes: list [Class]):
        self.name = name
        self.classes = classes

    def print_all_classes(self):
        print('Список классов:')
        for item in self.classes:
            print(item.name)

    def print_parent(self, student):
        res = 0
        for item in self.classes:
            for i in item.students:
                if i.person.name == student.person.name and i.person.surname == student.person.surname:
                    res = 1
                    print('Родители {} {}:'.format(student.person.name, student.person.surname))
                    for parent in i.parents:
                        print(parent.person.get_full_name())
        if res == 0:
            print('Родители ученика не найдены')

    def print_all_subject_student(self, student):
        current_class = ''
        for item in self.classes:
            for i in item.students:
                if i.person.name == student.person.name and i.person.surname == student.person.surname:
                    current_class = item
        print('Предметы ', current_class.name)

        
        for teacher in current_class.teachers:
            print(teacher.subject.name)
        



list_Parent = [Parent('Иван', 'Рубильников'), Parent('Светлана', 'Рубильниккова')]
list_student = [Student('Кирилл', 'Рубильников', list_Parent)]
list_teacher = [Teacher('Андрей','Яблоков', Subject('Математика'))]
list_classes = [Class('7Б', teachers=list_teacher, students=list_student), Class('8Б', teachers=[], students=[])]

school = School('Гимназия №11', classes=list_classes)

school.print_all_classes()
school.classes[0].print_all_student()
school.print_parent(list_student[0])
school.classes[0].print_all_techer()
school.print_all_subject_student(list_student[0])
