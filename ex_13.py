count = 0
while True:
    ticket = input()
    count += 1
    n = len(ticket)
    if n % 2 != 0:
        continue
    polovina = n // 2
    first = ticket[:polovina]
    second = ticket[polovina:]
    sum_1 = sum(int(index) for index in first)
    sum_2 = sum(int(index) for index in second)
    if sum_1 == sum_2:
        print(count)
        break
