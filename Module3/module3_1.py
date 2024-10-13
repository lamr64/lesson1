calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)

print(string_info('Green bananas'))
print(string_info('Yellow apples'))
print(is_contains('packing', ['PACKing', 'UNpacking', 'pack']))
print(is_contains('feeling', ['FEEL', 'Felt', 'Felt']))
print(calls)