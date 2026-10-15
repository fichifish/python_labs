import random
import statistics

n = int(input())
if n<=0: print("не хочу робити дз")
else:
    grades = []
    for i in range(n): grades.append(random.randint(1, 12))
    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", statistics.mean(grades))
    print("Медіана:", statistics.median(grades))
    res = 0
    for i in grades:
        if i>=10: res+=1
    print("Оцінок 10-12:", res)