pay = int(input('Enter you pay: '))
if pay > 1000:
    if pay > 2000:
        Bonus = 100
    else:
        Bonus = 50
else:
    Bonus = 10
    
print('Pay:',pay)
print("Bonus:",Bonus)
print('Total:',pay + Bonus)