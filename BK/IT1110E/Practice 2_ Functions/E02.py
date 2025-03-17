def pascal_triangle(n):
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

    for i in range(n):
        row = [binomial_coefficient(i, k) for k in range(i + 1)]
        print(' '.join(map(str, row)))