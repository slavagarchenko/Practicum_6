str1 = input()
str2 = input()
str3 = input()
set1 = set(str1)
set2 = set(str2)
set3 = set(str3)
uniq_el = set()
for index in set1:
    if index not in set2 and index not in set3:
        uniq_el.add(index)
for index in set2:
    if index not in set1 and index not in set3:
        uniq_el.add(index)
for index in set3:
    if index not in set1 and index not in set2:
        uniq_el.add(index)
print(''.join(uniq_el))
