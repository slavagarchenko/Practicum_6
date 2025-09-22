import keyword
name = input()
if keyword.iskeyword(name):                        # Kлючевое слово
    print("Нет")
if name[0].isdigit():                              # Цифра
    print("Нет")
else:
    flag = 1
    for index in name:
        if not (index.isalnum() or index == '_'):  # Буква или цифра
            flag = 0
            break
    if flag == 1:
        print("Да")
    else:
        print("Нет")
