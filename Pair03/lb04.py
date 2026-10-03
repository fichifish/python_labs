
s = str(input())
words = s.split(" ")
words2 = s.lower().split(" ")
max_word_length = 0
min_word_length = len(words[0])
idk = 0
for word in words:
    if (len(word) > max_word_length):
        max_word_length = len(word)
    if (len(word) < min_word_length):
        min_word_length = len(word)
    if words2.count(word.lower()) == 1: idk+=1
longest_words = []
shortest_words = []
for word in words:
    if (len(word) == max_word_length and word not in longest_words): longest_words.append(word)
    if (len(word) == min_word_length and word not in shortest_words): shortest_words.append(word)
print("Найдовші: " + ", ".join(longest_words) + "\nНайкоротші: " + ", ".join(shortest_words) + "\nУнікальних слів: " + str(idk)) # чому в прикладі виводить 6 унікальних слів??
ChangedWord = str(input())
NewWord = str(input())
for word in words:
    if (word == ChangedWord): words[words.index(word)] = NewWord
print("Після заміни: " + " ".join(words))