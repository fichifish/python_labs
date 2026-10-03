s = str(input())
words = s.split(" ")
if len(words) == 3: print(words[0].capitalize() + " " + words[1][0].upper() + "." + words[2][0].upper() + ".")