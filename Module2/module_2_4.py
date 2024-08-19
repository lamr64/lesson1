numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    is_primes = True
    if num == 1:
        continue
    for i in range(2, num):
        if (num % i == 0):
            is_primes = False
    if is_primes == True:
        primes.append(num)
    else:
        not_primes.append(num)
print(primes)
print(not_primes)

# Должно вывести:
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
