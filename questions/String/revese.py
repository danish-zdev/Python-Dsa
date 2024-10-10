# output = 'WoH ErA UoY'

# string = 'How are you'
# output = ''
# for word in string.split():
#     output += word[::-1] + ' '
# print(output[:-1].swapcase().lower())

# string = 'How are you'
# output = ' '.join([word[::-1] for word in string.split()]).lower().swapcase()
# print(output)

# string = 'How are you'
# output = ' '.join([word[::-1] for word in string.split()]).swapcase().title()
# print(output)


# string = 'How are you'
# output = ''
# for word in string.split():
#     reversed_word = word[::-1]
#     for i in range(len(reversed_word)):
#         if i % 2 == 0:
#             output += reversed_word[i].upper()
#         else:
#             output += reversed_word[i].lower()
#     output += ' '
# print(output[:-1])


string = 'How are you'
words = string.split()
output = words[0][0].upper() + words[0][1:][::-1]
for word in words[1:]:
    output += ' ' + word[::-1]
print(output)

