hr = float(input('Enter Hours:'))
rt = float(input('Enter Rate:'))

if hr > 40.0:
    pay = 40 * rt + (hr-40) * rt * 1.5
else:
    pay = hr*rt

print('Pay:',round(pay,2))