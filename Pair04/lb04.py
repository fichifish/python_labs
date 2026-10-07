group_info = ("10-IT", "2026/2027")
journal = {"Anna": [10, 11, 12, 9, 10], "Ivan": [8, 9, 10, 11, 9]} 

while True:
    name = str(input())
    if (name == ""): break
    grades = list(map(int, input().split()))
    if len(grades) != 5: continue
    journal[name] = grades

average = {}
print(" ".join(group_info))
for student, grades in journal.items(): 
    print(student + ": " + ", ".join(map(str, grades)))
    average[student] = sum(grades)/len(grades)
print("Середнє:")
for student, avg in average.items(): print(student + " - " + str(avg))
sortedd = sorted(average.items(), key=lambda x: x[1], reverse=True)
print("Рейтинг:")
count = 0
for student, avg in sortedd: count += 1; print(str(count) + ". " + student + " - " + str(avg))
print("Як же він харош:\n" + sortedd[0][0] + " - " + str(sortedd[0][1]))