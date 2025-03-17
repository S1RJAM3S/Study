n = int(input())
def sum_of_digits(n: int) -> int: return n if len(str(n)) == 1 else int(str(n)[-1]) + sum_of_digits(int(str(n)[0:-1]))
print(sum_of_digits(n))