# extract the floating point number
str = 'X-DSPAM-Confidence: 0.8475'

index = str.find(' ')
num = float(str[index+1:])

print(num)
