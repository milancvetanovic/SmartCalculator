from parsing_math_expressionn import parse_math_expression

expression = input().strip()


def infix_to_postfix(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    postfix_expression = []
    stack = []

    for item in expression:
        try:
            postfix_expression.append(int(item))
        except ValueError:
            if item == '(':
                stack.append(item)
            elif item == ')':
                while stack[-1] != '(':
                    postfix_expression.append(stack.pop())
                stack.pop()
            elif not stack or stack[-1] == '(' or operators[item] > operators[stack[-1]]:
                stack.append(item)
            else:
                while stack and stack[-1] != '(' and operators[item] <= operators[stack[-1]]:
                    postfix_expression.append(stack.pop())
                stack.append(item)

    while stack:
        postfix_expression.append(stack.pop())

    return postfix_expression


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


expression = parse_math_expression(expression)
print(expression)
print(infix_to_postfix(expression))
# if expression:
#     infix_expression = infix_to_postfix(expression)
#     print(calculate_postfix_expression(infix_expression))
# else:
#     print("Invalid expression")
