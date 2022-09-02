operators = {'+': 1, '-': 1, '*': 2, '/': 2}
postfix_expression = []
stack = []

expression = input().split()

for item in expression:
    try:
        postfix_expression.append(int(item))
    except ValueError:
        if not stack or stack[-1] == '(' or item == '(':
            stack.append(item)
        elif item == ')':
            while stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()
        elif operators[item] > operators[stack[-1]]:
            stack.append(item)
        else:
            while stack and stack[-1] != '(' and operators[item] <= operators[stack[-1]]:
                postfix_expression.append(stack.pop())
            stack.append(item)

while stack:
    postfix_expression.append(stack.pop())


def calculate_postfix_expression(tokens):
    result = []

    for element in tokens:
        if type(element) == int:
            result.append(element)
            continue

        operand2 = result.pop()
        operand1 = result.pop()
        if element == '+':
            result.append(operand1 + operand2)
        elif element == '-':
            result.append(operand1 - operand2)
        elif element == '*':
            result.append(operand1 * operand2)
        elif element == '/':
            result.append(operand1 / operand2)

    return result.pop()


print(postfix_expression)
print(calculate_postfix_expression(postfix_expression))
