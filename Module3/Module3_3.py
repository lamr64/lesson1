def print_params(a=5, b='Hello, World', c=True):
    print(a, b, c)
    return
print_params(2,'seven')

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (12, [17, 3, 5], True)
values_dict = {'a': 1234, 'b': 3456, 'c': 4567}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, 'Python']
print_params(*values_list_2, 42)
