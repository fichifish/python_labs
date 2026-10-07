# шошо? хто цю умову писав?

idk = {"Карась": 2, "Окунь": 3, "Ракета": 500000, "Шахед": 20000}

name = input("Назва: ").strip()
price = float(input("Ціна: "))
idk[name] = price
print(idk)

name2 = input("Назва: ").strip()
price2 = idk.get(name2)
if price2: print("Ціна:", price2)
else: print("Нема такого")

l = float(input())
r = float(input())
for a, b in idk.items():
    if l <= b and b <= r: print(str(a) + ": " + str(b), end="; ")