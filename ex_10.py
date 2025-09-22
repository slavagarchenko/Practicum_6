sentence = input()
words = sentence.split()
first_word = words[0]
for word in words[1::]:
    if word != first_word and len(word) == len(set(word)):
        print(word)
