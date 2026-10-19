students = ["fish", "artem", "mosquito"]
grades = {"math":12, "programming":12, "history":9}
try:
    a = int(input("1 - учень, 2 - предмет: "))
    if (a==1): 
        try:
            b = int(input("Індекс: "))
            print(students[b])
        except ValueError: print("потрібно ввести ціле число.")
        except IndexError: print("потрібно ввести валідний індекс.")
    else:
        try:
            b = input("Назва: ")
            print(grades[b])
        except KeyError: print("потрібно ввести валідний предмет.")
except ValueError: print("потрібно ввести 1 або 2.")