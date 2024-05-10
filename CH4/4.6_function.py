# notice in python function doesn't have to be declared before use (like c)
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print(type(print_lyrics)) # function is defined as object in Python

repeat_lyrics()