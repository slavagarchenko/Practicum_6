from num2words import num2words
number = input()
number = number.replace(' ', '')
number = int(number)
print(num2words(number, lang='ru'))
