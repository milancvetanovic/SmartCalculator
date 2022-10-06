def invalid_chars(expression):
    for char in expression:
        if not char.isalnum() and char not in ('+', '-', '*', '/', '(', ')', ' ', '^'):
            return True

    return False


def check_first_char(first_char):
    if first_char in ('*', '/', ')', '^'):
        return True
    return False


def check_last_char(last_char):
    if last_char in ('+', '-', '*', '/', '(', '^'):
        return True
    return False


def check_neighboring_elements(expression):
    for i in range(len(expression) - 1):
        if expression[i].isalnum() and expression[i + 1].isalnum():
            return True
        elif expression[i].isalnum() and expression[i + 1] == '(':
            return True
        elif expression[i] in ('+', '-', '*', '/', '^') and expression[i + 1] in ('*', '/', ')', '^'):
            return True
        elif expression[i] == '(' and expression[i + 1] in (')', '*', '/', '^'):
            return True
        elif expression[i] == ')' and expression[i + 1] == '(':
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


def check_var_name(var_name):
    if var_name.isalnum():
        if var_name[0].isdigit():
            return True
        return False
    return True


def check_variables(expression, var_list):
    for i, item in enumerate(expression):
        if item.isalnum():
            if item.isnumeric():
                continue
            elif check_var_name(item):
                print("Invalid identifier")
                return None
            else:
                try:
                    expression[i] = var_list[item]
                except KeyError:
                    print("Unknown variable")
                    return None

    return expression
