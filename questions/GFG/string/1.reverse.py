def reverseWords(S):
    # S = "i.like.this.program.very.much"
    words = S.split(".")
    # words.reverse()
    # result = ".".join(words)
    st = ""
    for i in S:
        i+=st
    print(st)    
    # result = ".".join(words)


    return 

    # print(result)
S = "i.like.this.program.very.much"
print(reverseWords(S))

# mystr  = "avb$cdee!"
# lst = []
# str = ""
# for i in (mystr.split()):
#     letter = [word for word in i if i.isalpha]
#     print(letter)
#     for word in i:
#         if word.isalpha():
#             lst.append(letter.pop())
#             continue
#         lst.append(word)

# print(''.join(lst))
 


# def rev(str):
#     strnw = str.split(' ')
#     str1 = strnw[::-1]
#     new = ' '.join(str1)
#     return new

# str = "i love greekforgreek"
# print(rev(str))



# mystr  = "123$$32@1!$"

# str = ""
# spc = "$!@"
# for i in mystr.split():
#      if spc in str:
#          str =  i+str
#          continue
#      str = i+str
# print(str)
# str_smpl = 'String;2bereversed...'
# lst = []
# for word in str_smpl.split():
#     print(word)
#     print('&&&&&&&&&&&&&&&')
#     letters = [c for c in word if c.isalpha()]
#     print(letters)
#     print('----------')
#     for c in word:
#         if c.isalpha():
#             lst.append(letters.pop())
#             print(lst)
#             print('????????????????')
#             continue
#         else:
#             lst.append(c)
#             print(lst)
#             print('----------')
#     lst.append(' ')
#     print(lst,"werewrwere")
# print("".join(lst))



# ml = []
# for i in mystr.split():
#     lettr = [c for c in i if c in c.isalpha()]
#     for c in i:
#        if c.isalpha():
#             ml.append(c.pop)
#             continue
#        else:
#             ml.append(c) 
# print("".join(ml))



def reverse_string_without_affecting_number(text):
    temp = []
    text = list(text)
    for i in text:
        if not i.isnumeric():
            temp.append(i)
    reverse_temp =  temp [::-1]
    count = 0
    for i in range(0,len(text)):  
        if not text[i].isnumeric():
            text[i] = reverse_temp[count]
            count +=1  
        else:
            continue
    return "".join(text)
    
print (reverse_string_without_affecting_number('abc1235de9f15ui')) 

