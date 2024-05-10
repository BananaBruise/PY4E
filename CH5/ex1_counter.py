total = 0
count = 0
# read integer until user enters "done"
while True:
    num = input("Enter a number: ")
    # quit if done
    if num == 'done':
        break
    
    # cast to int
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    # calculate statistics
    count+=1
    total+=num

# print total, count, and average
print(total, count, round(total/count, 2))