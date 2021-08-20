# Everything is an object
print(isinstance(4, object))
print(isinstance("Michael", str))
print(isinstance([], object))
print(isinstance(None, object))
print(isinstance(str, object))
print(isinstance(object, object))

# diffrence between object and variable:
"""
objects have identity, type, and value
variables are un-typed(dynamically typed)
"""

# identity
print(id(None))

# type
print(type(None))
print(isinstance(type(None), object)) # Types are also objects

# value
print((None).__sizeof__()) # Objects contains pointers to their underlying data bolb
# 16 bytes
print((1).__sizeof__()) # 28 bytes
# small things take up a lot of memories

# variable assignment does not copy the object, it create a reference to the object
