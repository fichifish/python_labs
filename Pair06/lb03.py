from datetime import date

a, b, c = map(int, input().split("-"))
one = date(a, b, c)
two = date.today()
res = abs(one-two)
if one > two: print("До події залишилося:", res.days, "днів")
elif one < two: print("Після події минуло:", res.days, "днів")
else: print("Це сьогодні")