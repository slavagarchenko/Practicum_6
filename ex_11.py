cities = input().split()
for i in range(1, len(cities)):
    presennt_step = cities[i].lower()
    past_step = cities[i - 1].lower()
    last_letter = past_step[-1]
    if last_letter == 'ь' and len(past_step) > 1:
        last_letter = past_step[-2]
    first_letter = presennt_step[0]
    if last_letter != first_letter:
        if i % 2 == 1:
            print("Петя")
        else:
            print("Вася")
        break
else:
    if len(cities) % 2 == 1:
        print("Петя")
    else:
        print("Вася")
