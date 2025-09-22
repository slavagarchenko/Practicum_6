text = input()
for index in text:
    if text.count(index) == 3:
        print(index)
        break
