from parsing_math_expression import parse_math_expression
from infix_to_postfix import infix_to_postfix, calculate_postfix_expression
from check_validity import check_var_name, check_variables


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
        else:
            assigned_value = check_variables(assigned_value, self.variables)

            if assigned_value == "Unknown variable":
                return "Unknown variable"

            if assigned_value == "Invalid identifier":
                return "Invalid identifier"

        assigned_value = infix_to_postfix(assigned_value)
        self.variables[operators[0]] = calculate_postfix_expression(assigned_value)
        return None

    def handle_expression(self, express):
        if not express.strip():
            return "Type something"

        express = parse_math_expression(express)

        if not express:
            return "Invalid expression"

        express = check_variables(express, self.variables)

        if express == "Unknown variable":
            return "Unknown variable"

        if express == "Invalid identifier":
            return "Invalid identifier"

        postfix_express = infix_to_postfix(express)

        return str(calculate_postfix_expression(postfix_express))
