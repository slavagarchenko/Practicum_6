text = input()
tickets = text.split(" ") 

for ticket in tickets:
    if len(ticket) % 2 == 0:  
        mid = len(ticket) // 2
        first_half = ticket[:mid]
        second_half = ticket[mid:]
        
        sum_first = sum(int(digit) for digit in first_half)
        sum_second = sum(int(digit) for digit in second_half)
        
        if sum_first == sum_second:
            print(ticket)
