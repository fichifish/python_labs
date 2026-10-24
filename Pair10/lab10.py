# class Person:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         return f"Учень: {self.name}"
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#     def info(self):
#         return f"Учень: {self.name}, група: {self.group}"
# student = Student("Kobets Artem", "IT-10")
# student1 = Student("Old Kobets Artem", "BSM")
# print(student.info())
# print(student1.info())



# class Teacher(Person):
#     def __init__(self, name, subject):
#             super().__init__(name)
#             self.subject = subject
#     def info(self):
#         return f"Викладач: {self.name}, предмет: {self.subject}"
# someone = [Student("Kobets Artem", "IT-10"), Teacher("Mosquito", "informatics"), Student("fish", "IT-10"), Teacher("Tadla", "math")]
# for i in someone: print(i.info())



# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#     def add_student(self, student):
#         flag = True
#         for i in self.students:
#             if i.name == student.name: 
#                 flag = False
#                 break
#         if flag: self.students.append(student)
#     def remove_student(self, name):
#         for i in self.students:
#             if i.name == name: 
#                 self.students.remove(i)
#                 break
#     def show_students(self):
#         print(f"Курс: {self.title}")
#         print(f"Викладач: {self.teacher.name}")
#         print("Студенти:")
#         for i, j in enumerate(self.students, 1):
#             print(f"{i}. {j.name}, група: {j.group}")
# teacher = Teacher("Mosquito", "informatics")
# student = Student("Artem", "BSM")
# student1 = Student("Fish", "IT-10")
# student2 = Student("Skittles", "Shop")
# student3 = Student("Sail ship", "Water")
# python_course = Course("Python", teacher)
# python_course.add_student(student)
# python_course.add_student(student)
# python_course.add_student(student1)
# python_course.add_student(student3)
# python_course.add_student(student2)
# python_course.remove_student("Skittles")
# python_course.show_students()




course_data = r"C:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair10\course_data.txt"

class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        return f"Учень: {self.name}"
class Student(Person):
    def __init__(self, name, group, grades=None):
        super().__init__(name)
        self.group = group
        if grades is None: self.grades = []
        else: self.grades = grades
    def info(self):
        return f"Учень: {self.name}, група: {self.group}"
    def add_grade(self, grade):
        if 1<=grade<=12: self.grades.append(grade)
    def average(self):
        if len(self.grades)==0: return 0
        return sum(self.grades)/len(self.grades)
class Teacher(Person):
    def __init__(self, name, subject):
            super().__init__(name)
            self.subject = subject
    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
        self.read()
    def find_student(self, name):
        for i in self.students:
            if i.name == name:
                return i
        return None
    def add_student(self, student):
            if self.find_student(student.name) is None: self.students.append(student)
    def remove_student(self, name):
        idk = self.find_student(name)
        if idk!=None: self.students.remove(idk)
    def add_grade_to_student(self, name, grade):
        idk = self.find_student(name)
        if idk: return idk.add_grade(grade)
    def show_students(self):
            print(f"Курс: {self.title}")
            print(f"Викладач: {self.teacher.name}")
            print("Студенти:")
            for i, j in enumerate(self.students, 1):
                print(f"{i}. {j.name}, група: {j.group}")
    def show_rating(self):
        print("Рейтинг:")
        sort = sorted(self.students, key=lambda x: x.average(), reverse=True)
        for i, j in enumerate(sort, 1):
            print(f"{i}. {j.name} - {j.average()}")
    def write(self):
        try:
            with open(course_data, "w", encoding="UTF-8") as file:
                for i in self.students:
                    res = []
                    for j in i.grades:
                        res.append(str(j))
                    file.write(f"{i.name};{i.group};{",".join(res)}\n")
        except Exception as idk: print(f"Помилка: {idk}")
    def read(self):
        try:
            with open(course_data, "r", encoding="UTF-8") as file:
                for line in file:
                    line = line.strip()
                    s = line.split(";")
                    if len(s) >= 2:
                        name = s[0]
                        group = s[1]
                        grades = []
                        if len(s)>2 and s[2]:
                            for i in s[2].split(","):
                                try: grades.append(int(i))
                                except ValueError: pass
                        self.add_student(Student(name, group, grades))
        except FileNotFoundError: pass
        except Exception as idk: print(f"Помилка: {idk}")

teacher = Teacher("Mosquito", "informatics")
course = Course("C++", teacher)
print("1 - показати курс;\n2 - додати студента;\n3 - видалити студента;\n4 - знайти студента;\n5 - виставити оцінку;\n6 - показати рейтинг;\n7 - зберегти дані;\n0 - вихід.")
while True:
    try: 
        idk = int(input())
        if idk==0: break
        if idk==1: course.show_students()
        if idk==2: 
            name = input("ПІБ: ")
            group = input("Група: ")
            course.add_student(Student(name, group))
        if idk==3:
            name = input("ПІБ: ")
            course.remove_student(name)
        if idk==4:
            name = input("ПІБ: ")
            student = course.find_student(name)
            if student: print(f"Знайдено: {student.info()} - {student.average()}")
            else: print("Нема.")
        if idk==5:
            name = input("ПІБ: ")
            try:
                grade = int(input("Оцінка: "))
                course.add_grade_to_student(name, grade)
            except ValueError:
                print("Введіть ціле число.")
        if idk==6: course.show_rating()
        if idk==7: course.write()
    except ValueError: print("Введіть ціле число.")