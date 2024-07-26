my_dict = {'Alex': 1990, 'Rick': 1988, 'Nick': 1991}
print(my_dict)
print(my_dict['Alex']) # тут мы выводим соответствующий имени год рождения
print(my_dict.get('Sergey')) # тут мы проверяем список на наличие человека
my_dict.update({'Kim': 1992,
                'Leon': 1989}) # тут мы добавляем 2-х новых людей
del my_dict['Rick']
my_dict.get('Rick') # тут снова проверка на наличие удаленной пары
print(my_dict['Nick'])
print(my_dict)
my_set = {7, 3, 4, 2, 5, 6, True, 'Urban'}
print(my_set)
my_set.add(10)
my_set.add(9)
my_set.discard(4)
print(my_set)



