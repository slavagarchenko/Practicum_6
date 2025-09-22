text = input().lower()
el = set()
for index in text:
    if index.isalpha():
        el.add(index)
print(len(el))
