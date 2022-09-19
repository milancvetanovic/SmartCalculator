def parse_math_expression(expression):
    expression = [char for char in expression]

    for char in expression:
        if not char.isalnum() and char not in ('+', '-', '*', '/', '(', ')', ' '):
            return None

    if expression[-1] in ('+', '-', '*', '/', '('):
        return None

    if expression[0] in ('*', '/', ')'):
        return None

    # Spaja cifre i slova u brojeve ili promenljive, ako su jedna do druge
    i = 0
    while i < len(expression) - 1:
        if expression[i].isalnum():
            for item in expression[i+1::]:
                if not item.isalnum():
                    break
                expression[i] += expression.pop(i+1)
        i += 1

    # Uklanja sve razmake iz liste
    expression = [item for item in expression if item != ' ']

    for i, _ in enumerate(expression):
        if expression[i].isalnum() and expression[i+1].isalnum():
            return None
        elif expression[i].isalnum() and expression[i+1] == '(':
            return None
        elif expression[i] in ('+', '-', '*', '/') and expression[i+1] in ('*', '/', ')'):
            return None
        elif expression[i] == '(' and expression[i+1] == ')':
            return None
        elif expression[i] == ')' and expression[i+1] == '(':
            return None

    i = 0
    while i < len(expression)-1:
        if expression[i] == '+':
            if expression[i+1] == '+':
                expression.pop(i+1)
                continue
            elif expression[i+1] == '-':
                expression.pop(i)
                continue
        elif expression[i] == '-':
            if expression[i+1] == '+':
                expression.pop(i+1)
                continue
            elif expression[i+1] == '-':
                expression[i] = '+'
                expression.pop(i+1)
                continue
        i += 1

    if expression[0] == '+':
        expression.pop(0)
    # elif expression[0] == '-':
    #     expression[0] += expression[1]
    #     expression.pop(1)

    # i = 0
    # while i < len(expression)-1:
    #     if expression[i] == '(' and expression[i+1] == '-':
    #         expression[i+1] += expression[i+2]
    #         expression.pop(i+2)
    #         continue
    #     i += 1

    stack = []
    for item in expression:
        if item == '(':
            stack.append(item)
        elif item == ')':
            try:
                stack.pop()
            except IndexError:
                return None

    if stack:
        return None

    return expression
