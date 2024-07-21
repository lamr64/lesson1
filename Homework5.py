immutable_var = (1, 2, 3, "Present", False, [7, 6])
print(type(immutable_var))
# immutable_var.remove("Present") нельзя заменить переменную в tuple
immutable_var = ([1, 3, 4], 7, 9, [8, 5]) # можно заменить полностью
print(immutable_var)
immutable_var[0][2] = 7 # тут заменили в 0-м списке переменную 2-ую на цифру 7
immutable_var = (7, 5, 6, False)
print(immutable_var)
# immutable_var[2][0] = True # тут мы видим, что внутри кортежа мы не можем менять переменные, только если это будет список, строка №7
mutable_list = (['Sergey', 'Anatoly', 'Maxim', 3, 4, 5]) # список, в котором можно заменить переменные
print(type(mutable_list))
name_1 = 'Grigory'
mutable_list.append(name_1) # тут мы добавили в наш список еще одно имя
mutable_list.extend(['Ruslan','Oleg']) # тут мы добавили еще 2 имени
to_remove = [3,4,5]
for x in to_remove:
    mutable_list.remove(x) # тут мы убрали лишние в списке переменные
print(mutable_list)
print([3, 4, 5] not in mutable_list) # тут мы проверяем что убрали лишнее из списка
print(int not in mutable_list) # тут мы проверяем, что в списке отсутствуют цифры




