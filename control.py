a = 0
if a:
    print('a')
elif a == 0:
    print('a == 0')
else:
    print('hello!')

# Zero values and empty data structures are "falsy"
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))

# Everything else is "truthy"
print(bool("a"))
print(bool([False]))

# Loop
"""
for item in iterable
   process(item)
"""   
# iterable generation:
# range(stop) or range(start, stop, step) generates an iterable over a range of numbers, same as string slicing, start is inclusive while stop is not inclusive
for ch in "CS41":
    print(ch)
for num in [3, 1, 4, 1, [4, 5]]:
    print(num)
for rangeitem in range(2, 12, 3):
    print(rangeitem)

# Break and Continue
for i in range(2, 10): # 2 - 9
    if i == 6:
        break
    print(i)

for letter in "UNICORN":
    if letter in "UN":
        continue
    print(letter)

# While loop
n = 0
while n < 1000:
    print(n)
    n += 100

