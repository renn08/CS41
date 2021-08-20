string = "I love you"

print("length:")
print(len(string))

print(string.find("I", 1)) # -1 if not found, otherwise, return the index of the first character of the subtext
print(string.replace("you", "Lu Xinyi"))
print(string.startswith("I"))
print(string.endswith("you"))
print(string.isalpha())
string_ = "a"
print(string_.isalpha())\

print(string.lower())
print(string.title())
print(string.upper())
print(string.strip())
print(string.strip('ou'))

print(list(string))
print(string.split())
print(string.split(sep = ' l'))
print(string.join(['Alice ', ' Bob ', ' Cindy']))

print('{} {}'.format('beautiful', 'girl'))
print('{0} like {0} and {1}'.format('Beautiful girls', 'boys'))
print('{name} loves {food}'.format(name = 'Mike', food = 'fish'))

print('{:06.2f}'.format(3.1415926))# 0 is the figure to fill in the blank, 6 is the width, 2 is the digit after the period, f is 靠右 
print('{:10}'.format('left'))
print('{:*^12}'.format('CS41'))
