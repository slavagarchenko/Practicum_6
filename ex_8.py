text = input()
text_1 = text.split()
cnt = sorted(text_1, key=len)
print(' '.join(cnt))
