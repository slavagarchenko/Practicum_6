text = input()
cnt = 0
maxcount = 0
last_el = None
for index in text:
    if last_el == index:
        cnt += 1
    else:
        if cnt > maxcount:
            maxcount = cnt
        last_el = index
        cnt = 1
if cnt > maxcount:
    maxcount = cnt
print(maxcount)
