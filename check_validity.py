def is_chars_valid(expression):
    for char in expression:
        if not char.isalnum() and char not in ('+', '-', '*', '/', '(', ')', ' ', '^'):
            return False
    return True


def is_last_char_valid(last_char):
    if last_char in ('+', '-', '*', '/', '(', '^'):
        return False
    return True


def is_first_char_valid(first_char):
    if first_char in ('*', '/', ')', '^'):
        return False
    return True


def check_neighboring_elements(expression):
    for i in range(len(expression) - 1):
        if expression[i].isalnum() and expression[i + 1].isalnum():
            return False

        if expression[i].isalnum() and expression[i + 1] == '(':
            return False

        if expression[i] in ('+', '-', '*', '/', '^') and expression[i + 1] in ('*', '/', ')', '^'):
            return False

        if expression[i] == '(' and expression[i + 1] in (')', '*', '/', '^'):
            return False

        if expression[i] == ')' and expression[i + 1] == '(':
            return False

    return True


def check_brackets(expression):
    stack = []
    for item in expression:
        if item == '(':
            stack.append(item)
            continue

        if item == ')':
            if not stack:
                return False
            stack.pop()

    if stack:
        return False

    return True


def check_var_name(var_name):
    if var_name.isalnum():
        if var_name[0].isdigit():
            return False
        return True
    return False


def check_variables(expression, var_list):
    for i, item in enumerate(expression):
        if item.isalnum():
            if item.isnumeric():
                continue

            if not check_var_name(item):
                return "Invalid identifier"

            try:
                expression[i] = var_list[item]
            except KeyError:
                return "Unknown variable"

    return expression
