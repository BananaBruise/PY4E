import random

# default: rand between [0,1)
print('default rand')
for i in range(10):
    x = random.random()
    print(x)

# random int within range (inclusive high and low)
print('randint()')
for i in range(10):
    x = random.randint(5,10)
    print(x)

# random given list
print('choice()')
t = [1,2,3]
for i in range(10):
    x = random.choice(t)
    print(x)