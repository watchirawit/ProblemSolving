my_dict = {'Dave':'001','Ava':'002','Joe':'003'}
print(my_dict)
print(my_dict.values())
print(my_dict.get('Ava'))

print (type(my_dict))

new_dict = dict(Boss = '143',baitong = '23')
print(new_dict)
print (type(new_dict))
#---------------------
my_dict['Dava'] = '004'
my_dict['Chris'] = '003'
print('After update',my_dict)