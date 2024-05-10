min = None
max = None

# ask for input until 'done'
while True:
    num = input('Enter a number: ')

    # done
    if num == 'done':
        break

    # invalid input
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    # min/max
    if min == None or num < min:
        min = num
    if max == None or num > max:
        max = num

print("min:", min, "max:", max)