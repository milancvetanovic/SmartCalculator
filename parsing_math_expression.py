from check_validity import *


def parse_math_expression(expression):
    expression = [char for char in expression]

    if invalid_chars(expression):
        return None

    # Connects digits and chars in numbers and variables
    expression = nums_and_vars(expression)

    # Removes all spaces from the list
    expression = [item for item in expression if item != ' ']

    if check_neighboring_elements(expression):
        return None

    if check_brackets(expression):
        return None

    expression = plus_minus_signs(expression)

    if expression[0] == '+':
        expression.pop(0)

    return expression


def nums_and_vars(expression):
    i = 0
    while i < len(expression) - 1:
        if expression[i].isalnum():
            for item in expression[i + 1::]:
                if not item.isalnum():
                    break
                expression[i] += expression.pop(i + 1)
        i += 1

    return expression


def plus_minus_signs(expression):
    i = 0
    while i < len(expression) - 1:
        if expression[i] == '+':
            if expression[i + 1] == '+':
                expression.pop(i + 1)
                continue
            elif expression[i + 1] == '-':
                expression.pop(i)
                continue
        elif expression[i] == '-':
            if expression[i + 1] == '+':
                expression.pop(i + 1)
                continue
            elif expression[i + 1] == '-':
                expression[i] = '+'
                expression.pop(i + 1)
                continue
        i += 1

    return expression
