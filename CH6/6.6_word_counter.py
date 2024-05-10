def word_counter(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

word = input('Enter word: ')
letter = input('Enter letter: ')
print("letter count:",word_counter(word, letter))