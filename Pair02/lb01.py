n = int(input())
suma = 0
num = 0
if (n>=3):
    for i in range(1, n+1):
        if (i%3==0 or i%5==0):
            suma += i
            num += 1
    print("Кількість:", num, "\nСума:", suma, "\nСереднє:", suma/num)
else:
    print("Кількість: 0\nСума: 0\nСереднє: 0")