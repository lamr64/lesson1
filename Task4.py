food = ["apple", "coconut", "banana"] # список через запятую в кавычках, могут быть как слова, так значения или команды
# print(food[0]) # выбираем номер по порядку для отображения от 0 и далее
food[0] = "peach" # для замены в списке, необходимо выбрать номер переменной и обозначить, чем заменить
food.append(True) # позволяет добавить в список в конец новую переменную
food.extend("watermelon") # добавит слово, но по отдельным буквам как отдельные переменные
food.extend(["melon", 6]) # добавит в конце все переменные, в том виде, как введены, [] - важно учесть
food.remove("peach")
# print(food)
# основные команды являются - .append, .extend, .remove
# print("banana" in food) # для проверки наличия переменной в строке списка (True/False) в консоли
# print("peach" not in food) # для проверки отсутствия переменной в строке списка (True/False) в консоли
# print(food[:3]) # для отображение от 0 до 3 переменных, 0,1,2 переменные

tuple_ = 1, 2, 3, 4, True, 'String' # кортеж из переменных
list = [1, 2, 3, 4, True, 'String']
print(tuple_.__sizeof__()) # тут мы видим, что кортеж занимает меньше памяти, но он не изменяем
print(list.__sizeof__()) # тут мы видим, что список занимает больше памяти, зато может изменятся
tuple_ = ([1, 2], 0, [7, 8, 9]) # можно изменять полностью, но нельзя изменять частично
print(tuple_)
tuple_[2][1] = 2 # Возможно заменить все таки в кортеже списки (заменили 1-ую переменную от 0 в списке 2)
print(tuple_)
tuple_ = ([1, 2], 0) + (7,9) # может добавлять переменные через математические знаки
print(tuple_)
tuple_ = (1, 2) * 3 # благодаря умножению на переменную - списков внутри кортежа будет - 3
print(tuple_)
# tuple_2 = (1, 2, 3, 4)
# tuple_3 = tuple([1, 2, 3, 4])

