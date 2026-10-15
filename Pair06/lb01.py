import math

r = float(input())
a, b = map(int, input().split(", "))
n = int(input())
k = int(input())

print("Площа круга:", round(math.pi*(r**2), 2))
print("Гіпотенуза:", round(math.sqrt(a**2+b**2), 2))
print("Потрібно упаковок:", math.ceil(n/k))