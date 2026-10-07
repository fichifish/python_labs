idk = list(map(int, input().split()))
dodatni = []
videmni = []
parni = []
kratni = []
minn = idk[0]
maxx = idk[0]
summ = 0
for i in idk:
    if i >= 0:
        dodatni.append(i)
    else:
        videmni.append(i)
    if i % 2 == 0:
        parni.append(i)
    if i % 3 == 0:
        kratni.append(i)
    minn = min(minn, i)
    maxx = max(maxx, i)
    summ += i
print("Додатні:", dodatni)
print("Від'ємні:", videmni)
print("Парні:", parni)
print("Кратні 3:", kratni)
print("Min: " + str(minn) + "; Max: " + str(maxx) + "; Sum: " + str(summ) + "; Average: " + str(summ / len(idk)))