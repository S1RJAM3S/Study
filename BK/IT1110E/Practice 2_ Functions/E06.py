def dec_to_bin(n: int) -> str: return '1' if n == 1 else dec_to_bin(n//2) + str(n%2)