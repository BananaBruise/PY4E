# prompts user for hours and rate per hour to compute gross pay
hr = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
print("Pay:",round(hr*rt, 2))