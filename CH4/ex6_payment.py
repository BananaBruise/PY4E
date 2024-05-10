def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate
    
hr = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
print(computepay(hr, rt))