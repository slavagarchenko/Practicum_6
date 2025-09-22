def number_check(attempt, number):
    bulls = 0
    cows = 0
    for numb in attempt:
        if numb in number and attempt.find(numb) == number.find(numb):
            bulls += 1
        if numb in number and attempt.find(numb) != number.find(numb):
            cows += 1
    return f'Быков: {bulls}, Коров: {cows}'
number = input('Введите загаданное число')
print('\n' * 25)
step = 0
flag = 0
bulls = 0
cows = 0
while step <= 10 and flag == 0:
    attempt = input()
    step += 1
    if attempt == number:
        print('Победа!')
        flag = 1
    else:
        print(number_check(attempt, number))
if flag == 0:
    print('Проигрыш!')
