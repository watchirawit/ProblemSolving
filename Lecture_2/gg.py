Principal = int(input('Principal: '))
Interest = int(input('Interest: '))
Years = int(input('Years: '))
Time = int(input('Time: '))

Amount = Principal * (1 + Interest / Time) ** (Years * Time)

print('Amount:',Amount)
print('Principal:',Principal)
print('Interest:',Interest)
print('Years:',Years)
print('Time:',Time)