# input with prompt
input = input("please enter your street number: ")
print(type(input),'value:',input)

# input is string by default; recase to int using int()
integer = int(input) + 3
print(type(integer),'value:',integer)

# recast to float()
float = float(input) + 2.5
print(type(float),'value:',float)