import sys

def computegrade(score):
    if score < 0.0 or score > 1.0:
        return 'Bad score'

    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'
    
try:
    s_input = float(input("Enter score: "))
except:
    print('Bad score')
    sys.exit(1)

print(computegrade(s_input));