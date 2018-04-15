# coding: utf-8
# Author: Júlia Fernandes Alves <juliafealves@gmail.com>
# Handle: juliafealves
# Problem: B. Tanya and Postcard

SIZE_LETTER = 26

string_a = raw_input()
string_b = raw_input()


# Count the upper letters and lower letters.
def count_letters(string, list_lower, list_upper):
    for letter in string:
        if letter.islower():
            position = ord(letter) - ord('a')
            list_lower[position] += 1
        else:
            position = ord(letter) - ord('A')
            list_upper[position] += 1


# Add each letter in the list.
lower_letters_a = [0] * SIZE_LETTER
upper_letters_a = [0] * SIZE_LETTER
count_letters(string_a, lower_letters_a, upper_letters_a)

lower_letters_b = [0] * SIZE_LETTER
upper_letters_b = [0] * SIZE_LETTER
count_letters(string_b, lower_letters_b, upper_letters_b)

yay = 0
whoops = 0

for s in xrange(SIZE_LETTER):
    count_letter = min(lower_letters_a[s], lower_letters_b[s])
    lower_letters_a[s] -= count_letter
    lower_letters_b[s] -= count_letter
    yay += count_letter

    count_letter = min(upper_letters_a[s], upper_letters_b[s])
    upper_letters_a[s] -= count_letter
    upper_letters_b[s] -= count_letter
    yay += count_letter

    whoops += min(lower_letters_a[s], upper_letters_b[s])
    whoops += min(lower_letters_b[s], upper_letters_a[s])

print '%i %i' % (yay, whoops)
