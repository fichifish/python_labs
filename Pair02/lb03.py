n = int(input())
for i in range(1, n):
    flag = False
    t = i
    while (t>0):
        d = t%10
        if (d!=0 and i%d!=0): 
            flag = True
            break
        t //= 10
    if (flag == False): print(i, end=" ")