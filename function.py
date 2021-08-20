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

print(not True)
print(True or False)
print(True and False)

while True:
    try:
        n = int(input("input a int:"))
        break
    except ValueError as e:
        print("Invalid input. Try again...")
        print(e) # will output invalide literal for int() with base 10: 'int'
    # except SyntaxError as e_1:
    #   print(e_1)

"""
try:
    some_dangerous_code()
except SomeError as e:
    handle_the_exception(e)
except AnotherError:
    handle_without_binding()
except (OneError, TwoError):
    handle_multiple_errors()
except:
    handle_wildcard() # wildcard catches everything
"""

a = [1, 2, "a", "fix", [2, 3]]
for item in a:
    print(item)


    