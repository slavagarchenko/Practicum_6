import keyword
name = input()
if keyword.iskeyword(name):                        # key world
    print("Нет")
if name[0].isdigit():                              # The number
    print("Нет")
else:
    flag = 1
    for index in name:
        if not (index.isalnum() or index == '_'):  # Letter or number
            flag = 0
            break
    if flag == 1:
        print("Да")
    else:
        print("Нет")
