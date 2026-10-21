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
        return f"{self.name} - {self.average()}"

students = [Student("Fish"), Student("Artem"), Student("Mosquito"), Student("Missile"), Student("Sail ship")]
students[0].add_grade(12); students[0].add_grade(12); students[0].add_grade(12)
students[1].add_grade(12);  students[1].add_grade(12)
students[2].add_grade(11); students[2].add_grade(12); students[2].add_grade(11)
students[3].add_grade(8);  students[3].add_grade(9);  students[3].add_grade(10)
students[4].add_grade(10); students[4].add_grade(12); students[4].add_grade(11)
for student in students:
    print(student)
bestOfTheBests = sorted(students, key=lambda x: x.average(), reverse=True)
maxx = bestOfTheBests[0].average()
print("Найкращий результат: ", end="")
for i in bestOfTheBests:
    if i.average()==maxx: print(f"{i}  ", end="")