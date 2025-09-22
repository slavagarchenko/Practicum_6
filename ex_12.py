import re
import keyword

name = input()

if not name:
    print("Нет")
elif keyword.iskeyword(name):
    print("Нет")
elif re.match(r'^[a-zA-Z_]\w*$', name):
    print("Да")
else:
    print("Нет")
