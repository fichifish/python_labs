n = int(input())
k = int(input())
p1 = int(input())
p2 = int(input())

print(int(n/k)*min(p1*k, p2) + min((n%k)*p1, p2))