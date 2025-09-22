hint = input('Введите подсказку: ')
word = input('Введите загаданное слово: ')
print('\n' * 25)
stars = '*' * len(word)
print(hint, f'\n{stars}')
step = 0
flag = 0
while step <= 10 and flag == 0:
    chose = int(input('Буква или слово (0 - буква, 1 - слово)? '))
    step += 1
    attempt = input()
    if chose == 1 and attempt == word:
        print('Победа!')
        flag = 1
    if chose == 0:
        if attempt in word:
            new_stars = ""
            for i in range(len(word)):
                if word[i] == attempt or stars[i] != '*':
                    new_stars += word[i]
                else:
                    new_stars += '*'
            stars = new_stars
            print(stars)
        else:
            print(stars)
    if '*' not in stars:
        print('Победа')
        flag = 1
if flag == 0:
    print('Проигрыш!')
