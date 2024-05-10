import sys
try:
    hr = float(input('Enter Hours:'))
    rt = float(input('Enter Rate:'))
except:
    print('Error, please enter numeric input')
    sys.exit(1)

print('Pay:',round(hr*rt,2))