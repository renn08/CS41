a = True
print(type(a))
print(b := 3 > 2 > 1)
print(type(b))
print(c := 3 > 2 > 4) 

#string type
str = "happypython.py"
#str[start:stop:step]
#start inclusive, stop not inclusive
print(str[2])      #p
print(str[:3])     #hap
print(str[1:8:2])  #appt
print(str[8:1:-2]) #hyyp
print(str[::-1])   #yp.nohtypyppah

#list type
empty = []
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
many_types = ["a", 1, 2, [4, 5]]

print(many_types)
print(many_types[3])    #[4, 5]
print(many_types[3][1]) #5
many_types.extend([4, 5, 6])
print(many_types) 
