import random
import statistics

def generate_grades(count):
    grades = []
    for i in range(count): grades.append(random.randint(1, 12))
    return grades

def average_grade(grades):
    return statistics.mean(grades)

def get_level(average):
    if average < 4: return "початковий"
    elif average < 7: return "середній"
    elif average < 10: return "достатній"
    else: return "високий"