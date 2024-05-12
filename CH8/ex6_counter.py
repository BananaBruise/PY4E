nums = list()

while True:
    num = input("Enter a number: ")
    if num.lower() == 'done':
        break

    try:
        num = int(num)
    except:
        print("Please enter valid integer")
        continue

    nums.append(num)

if len(nums) > 0:
    print('Maximum: ', max(nums))
    print('Minimum: ', min(nums))
    print('Average: ', round(sum(nums)/len(nums),2))
else:
    print('list empty')


