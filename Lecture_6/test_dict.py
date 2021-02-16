test_dicts = {'List Smith':'521-8976','John Smith':'521-1234','Sandra Dee':'521-9655','Ted Baker':'418-4165','Sam Doe':'521-5030'}
print(test_dicts.values())
print(test_dicts.get('Ted Baker'))
print(test_dicts)

for x in test_dicts:
    print(x)

for x in test_dicts.values():
    print(x)

for x,y in test_dicts.items():
    print(x,y)