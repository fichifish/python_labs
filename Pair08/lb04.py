students = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair08\students.txt"
report = r"c:\Users\Acer\OneDrive\Desktop\Informatics\Pairs\Pair08\report.txt"

res = []; yes = 0; no = 0
try:
    with open(students, "r", encoding="utf-8") as file:
        text = file.readlines()
        for i, j in enumerate(text, start=1):
            j = j.strip()
            try:
                line = j.split(";")
                if len(line) != 2: raise ValueError("не є у такому форматі: 'Прізвище Ім'я;Бал'.")
                name = line[0].strip()
                grade = int(line[1].strip())
                if grade<0 or grade>100: raise ValueError("бал поза діапазоном 0-100.")
                res.append((name, grade))
                yes+=1
            except ValueError as idk:
                if "invalid" in str(idk): idk = "бал - не ціле число."
                print(f"Рядок {i} пропущено: {idk}")
                no+=1
    res.sort(key=lambda x: x[1], reverse=True)
    with open(report, "w", encoding="utf-8") as file:
        for i in res: file.write(f"{i[0]};{i[1]}\n")
    print("Правильних записів:", yes)
    print(f"Пропущено:", no)
    print("Створено report.txt")
except FileNotFoundError:
    print("файл не знайдено.")