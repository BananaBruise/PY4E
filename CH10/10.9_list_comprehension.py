# normal
list_of_int_in_str = ['1','5','8','69']
list_of_int = list()

for num in list_of_int_in_str:
    list_of_int.append(int(num))

print(list_of_int)

# list comprehension = shorthand way for creating list using linear lookup logic
list_of_int_comp = [int(num) for num in list_of_int_in_str]

print(list_of_int_comp)