cnt = 0
maxcount = 0
text = input()
for index in text:
    if index == ' ':
        cnt += 1
    else:
        if cnt > maxcount:
            maxcount = cnt
        cnt = 0
print(maxcount)
