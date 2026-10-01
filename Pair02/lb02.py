n = int(input())
suma = 0
num = 0
maxx = 0
minn = 9
while (n>0):
    d = n%10
    suma += d
    num += 1
    maxx = max(maxx, d)
    minn = min(minn, d)
    n //= 10
if (n!=0): print("Кількість цифр:", num, "\nСума цифр:", suma, "\nНайбільша цифра:", maxx, "\nНайменша цифра:", minn)
else: print("Кількість цифр:", 1, "\nСума цифр:", 0, "\nНайбільша цифра:", 0, "\nНайменша цифра:", 0)