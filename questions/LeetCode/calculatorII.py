
def calculate(self, s: str) -> int:

    # Initialize the stack
    stack = []

    # Append an operand onto the stack based on an operator
    def append(operator, operand):
        if operator == "+":
            stack.append(operand)
        elif operator == "-":
            stack.append(-operand)
        elif operator == "*":
            stack.append(stack.pop() * operand)
        else:
            stack.append(int(stack.pop() / operand))

    # Initialize the current operator and operand
    operator, operand = "+", 0

    # Iterate through all characters in s
    for c in s:

        # If the current character is a digit,
        if c in "0123456789":

            # Append it to the current operand
            operand = operand * 10 + int(c)

        # Elif the current character is a operator,
        elif c in "+-*/":

            # Append the current operand onto the stack
            append(operator, operand)

            # Update the current operand and operator
            operator, operand = c, 0

    # Add the last operand onto the stack
    append(operator, operand)

    # Return the sum of all operands as the result
    return sum(stack)





# def calculate(s: str) -> int:
#     s = s.replace(" ", "")
#     s += '+'
#     st = []
#     num = 0
#     op = '+'
#     # num = ''
#     for i in s:
#         if i.isdigit():
#             num = (num*10)+int(i)
#             # num += i
#         else:
#             num = int(num)
#             if op == '+':
#                 st.append(num)
#             elif op == '-':
#                 st.append(-num)
#             elif op == '*':
#                 st.append(st.pop()*num)
#             elif op == '/':
#                 st.append(int(st.pop()/num))
#             # num = ''
#             num = 0
#             op = i
#     return sum(st)



s = "3+2*2"
print(calculate(s))