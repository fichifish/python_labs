a = input()
a, b = map(int, a.split(" "))

if (a>=0 and b>=0): print("I")
elif (a<0 and b>=0): print("II")
elif (a<0 and b<0): print("III")
else: print("IV")