def input_grade():
    while True:
        try:
            grade = int(input("Оцінка: "))
            if grade<1 or grade>12: raise ValueError("оцінка повинна бути від 1 до 12.")
            return grade
        except ValueError as res:
            if "invalid" in str(res): print("потрібно ввести ціле число.")
            else: print(res)
print("Прийнято:", input_grade())