def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(1))
print(is_prime(4))
"""
Functions do not have return types, def to define, return optional, implicitly returns None
"""



    