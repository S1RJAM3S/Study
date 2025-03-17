p = 29
x_list = [14, 6, 11]

for x in range (1, p):
    a = x ** 2 % p
    if a in x_list:
        print(x)
        break