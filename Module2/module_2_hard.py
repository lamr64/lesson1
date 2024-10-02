def password(n):
    pass_ = []
    for i in range(1, int(n)):
        for j in range(i + 1, int(n)):
            sum_pass = j + i
            if int(n) % sum_pass == 0:
                pass_.append(i)
                pass_.append(j)
    return pass_
result = password(input("Введите число от 3 до 20, чтобы подобрать пароль: "))
print(*result, sep="")
