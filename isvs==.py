x = None
y = None

print(id(x))
print(id(y))

print(x == y)
print(x is y)

# Always use is to check if is None
# since == checks for equivalency, which can alter, while is checks for identity

class Negator(object):
    def __eq__(self, other):
        return not other

thing = Negator()
#print(id(thing))
#print(id(None))
print("thing == None: " + str(thing == None))
print("thing is None: " + str(thing is None))

lst = [1, 2, 3]
print(lst == lst[:])# default step 1, the same as lst[::1]
print(lst is lst[:])