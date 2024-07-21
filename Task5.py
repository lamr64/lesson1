phone_book = {'Lee': 79176245233, 'Kent': 72223334444} # dict - список с обозначением номеров (например телефонная книга)
# print(phone_book['Lee']) # введя имя, в консоли выводиться заданный номер
phone_book['Lee'] = 88002005050 # тут мы меняем номер в нашей книге
phone_book['Christian'] = 89002005050 # если ввести несуществующее в списке значение, оно запишется в список
del phone_book['Lee'] # del - для удаления человека из книги
phone_book.update({'Rex': 88222005050,
                   'Arnold': 87772225050}) # благодаря .update мы можем добавлять несколько человек в книгу
# print(phone_book.get('Sergey')) # Если ввести имя, которое находиться в списке, консоль выведет номер, а если не существующее - напишет "None" т.е. отсутствие номера
a = phone_book.pop('Kent') # позволяет вытащить необходимое и привязать к переменной для вывода
print(phone_book)
list = [1, 2, 3]
list.pop(0) # тут видно, как .pop убрало переменную "1"
print(list)
print(a)
print(phone_book.keys()) # выводит список "ключей" людей которые есть в нашем словаре
print(phone_book.values()) # выводит список "номеров" которые есть в нашем словаре
print(phone_book.items()) # выводит "ключ+номер" отображается как первоначально
phone_book['Rex'] = 88222005050, 613266 # Добавляем дополнительные номера
print(phone_book)
# также dict удобно применять для хранения логинов и паролей пользователей.

set_ = {1, 3, 5, 7, 1, 4, 5, 3, 2, 6} # команда set выводить "уникальные" не повторяющиеся значения в последовательности, не выводя повторяющиеся значения.
print(type(set_))
set_ = {1, 3, 5, 7, 1, 4, 5, 3, 2, 6, 'String', False, (1, 2, 3)} # также в составе set могут быть разные типы данных, которые будут выведены в консоль, но обратим внимание, что последовательность меняется
print(set_)
list_ = [7, 4, 5, 1, 3, 2]
print(list_)
print(set(list_)) # также мы можем при помощи set выделить уникальные значения и выставить последовательность в list (списках)
list_.remove(1) # этой командой мы можем убрать переменную из списка, еще можно применить команду .discard(1) для удаления необходимой переменной
print(list_)
print(type(list_))
set_.add(9) # .add помогает добавить в список set переменные