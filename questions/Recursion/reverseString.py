def reverseWord(s):
    #your code here
    if len(s) == 0:
        return s
    else:
        return reverseWord(s[1:]) + s[0]
s = 'Geeks'

print(reverseWord(s))