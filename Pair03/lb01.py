s = str(input())
words = s.split(" ")
letters = 0
digits = 0
spaces = 0
vowels = 0
for c in s:
    if (c.isalpha()):
        letters += 1
    if (c.isdigit()):
        digits += 1
    if (c.lower() in "aeiou"):
        vowels += 1
    if (c == " "):
        spaces += 1
print("Символів: " + str(len(s)) + "\nЛітер: " + str(letters) + "\nЦифр: " + str(digits) + "\nПробілів: " + str(spaces) + "\nГолосних: " + str(vowels) + "\nСлів: " + str(len(words)))