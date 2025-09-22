text = input()
cnt = 0
for index in text:
    if index == '(':
        cnt += 1
    if index == ')':
        cnt -= 1
if cnt == 0:
    print("True")
else:
    print("False")
