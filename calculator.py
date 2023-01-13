from parsing_math_expression import parse_math_expression, replace_variables
from infix_to_postfix import infix_to_postfix, calculate_postfix_expression
from check_validity import check_var_name


class SmartCalculator:
    def __init__(self):
        self.variables = {}

    def assignment(self, equation):
        if '=' not in equation:
            return "Invalid assignment"

        operators = [operator.strip() for operator in equation.split('=', 1)]

        if not check_var_name(operators[0]):
            return "Invalid identifier"

        assigned_value = parse_math_expression(operators[1])

        if not assigned_value:
            return "Invalid assignment"

        assigned_value = replace_variables(assigned_value, self.variables)

        if assigned_value in ("Unknown variable", "Invalid identifier"):
            return assigned_value

        assigned_value = infix_to_postfix(assigned_value)
        self.variables[operators[0]] = calculate_postfix_expression(assigned_value)

        return None

    def handle_expression(self, express):
        if not express.strip():
            return "Type something"

        express = parse_math_expression(express)

        if not express:
            return "Invalid expression"

        express = replace_variables(express, self.variables)

        if express in ("Unknown variable", "Invalid identifier"):
            return express

        postfix_express = infix_to_postfix(express)

        return str(calculate_postfix_expression(postfix_express))
