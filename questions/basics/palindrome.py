def is_palindrome(string):
    # string = str(string)
    return string == string[::-1]

print(is_palindrome("racecar"))
# print(is_palindrome(121))

