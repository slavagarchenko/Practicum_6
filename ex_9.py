sentence = input()
words = sentence.split()
uniq_word = set()
duplicate = None
for word in words:
    if word in uniq_word:
        duplicate = word
        break
    uniq_word.add(word)
print(duplicate)
