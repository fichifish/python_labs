class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    def add_grade(self, grade):
        try:
            if 1<=grade<=12: self.grades.append(float(grade))
            else: raise ValueError
        except: print(f"Оцінка {grade} не додається.")
    def average(self):
        if not self.grades: return 0
        return sum(self.grades)/len(self.grades)
    def __str__(self):
        return f"{self.name}: {self.grades}, середній = {self.average()}"

stud = Student("Artem Kobets")
stud.add_grade(12); stud.add_grade(11); stud.add_grade(24); stud.add_grade("A+")
print(stud)