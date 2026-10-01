w = int(input())
h = int(input())
n = str(input())
m = str(input())
for i in range(h):
    for j in range(w):
        if (i==0 or i==h-1 or j==0 or j==w-1): print(n, end="")
        else: print(m, end="")
    print()