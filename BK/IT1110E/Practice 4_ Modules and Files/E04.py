import math
import trig
n = int(input())

def custom_sum(n):
    result = 0
    for i in range(1, 21, 2):  
        result += trig.sin_m(n + i)
        result += trig.cos_m(n + i + 1)
    return round(result, 6)

def math_sum(n):
    result = 0
    for i in range(1, 21, 2):  
        result += math.sin(n + i)
        result += math.cos(n + i + 1)
    return round(result, 6)


custom_result = custom_sum(n)
math_result = math_sum(n)
print(f"Your own implementation:     {custom_result}")
print(f"Math module implementation:  {math_result}")
print()