file_path = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair07\text.txt"
file_path_students = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair07\students.txt"
file_path_result = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair07\result.txt"
file_path_grades = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair07\grades.csv"
file_path_report = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair07\report.txt"

# with open(file_path, "r", encoding="UTF-8") as file:
#     text = file.readlines()
# words = 0
# chars = 0
# maxI = 0
# maxx = 0
# maxText = ""
# for i, s in enumerate(text):
#     if len(s.rstrip("\n")) > maxx:
#         maxx = len(s.rstrip("\n"))
#         maxI = i+1
#         maxText = s
#     for c in s.split(): words+=1
#     chars+=len(s)
# print("Рядків:", len(text))
# print("Слів:", words)
# print("Символів:", chars)
# print(f"Найдовший рядок: №{maxI}, {maxx} символів")
# print("Текст:", maxText)

# with open(file_path, "r", encoding="UTF-8") as file:
#     text = file.readlines()
# a = input().strip().lower()
# flag = False
# for i, s in enumerate(text):
#     if a in s.lower():
#         print(f"{i+1}: {s.strip()}")
#         flag = True
# if not flag: print("Ти шось шукав?..")

# with open(file_path_students, "r", encoding="UTF-8") as file:
#     text = file.readlines()
# students = []
# for s in text:
#     name, score = s.strip().split(";")
#     if int(score) > 80: students.append((name, int(score)))
# students.sort(key = lambda x: x[1], reverse = True)
# with open(file_path_result, "w", encoding="UTF-8") as file:
#     for name, score in students: file.write(f"{name};{score}\n")

# with open(file_path_grades, "r", encoding="UTF-8") as file:
#     text = file.readlines()
# gradesIdk = {}
# for s in text:
#     name, subject, grade = s.strip().split(";")
#     if name not in gradesIdk: gradesIdk[name] = []
#     gradesIdk[name].append(float(grade))
# report = []
# for name, grades in gradesIdk.items(): report.append((name, len(grades), sum(grades)/len(grades)))
# report.sort(key=lambda x: x[2], reverse=True)
# awesome = report[0][2]
# bestOfTheBest = []
# for i in report:
#     if i[2] == awesome: bestOfTheBest.append(i[0])
# with open(file_path_report, "w", encoding="UTF-8") as file:
#     for name, count, avg in report:
#         file.write(f"{name} - оцінок: {count} - середній: {avg}\n")
#     file.write(f"Найкращий результат: {", ".join(bestOfTheBest)} - {awesome}")