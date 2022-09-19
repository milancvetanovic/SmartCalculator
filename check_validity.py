def invalid_chars(expression):
    for char in expression:
        if not char.isalnum() and char not in ('+', '-', '*', '/', '(', ')', ' '):
            return True

    if expression[-1] in ('+', '-', '*', '/', '('):
        return True

    if expression[0] in ('*', '/', ')'):
        return True

    return False


def check_neighboring_elements(expression):
    for i in range(len(expression)-1):
        if expression[i].isalnum() and expression[i+1].isalnum():
            return True
        elif expression[i].isalnum() and expression[i+1] == '(':
            return True
        elif expression[i] in ('+', '-', '*', '/') and expression[i+1] in ('*', '/', ')'):
            return True
        elif expression[i] == '(' and expression[i+1] == ')':
            return True
        elif expression[i] == ')' and expression[i+1] == '(':
            return True

    return False


def check_brackets(expression):
    stack = []
    for item in expression:
        if item == '(':
            stack.append(item)
        elif item == ')':
            try:
                stack.pop()
            except IndexError:
                return True

    if stack:
        return True

    return False
