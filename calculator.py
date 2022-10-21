from parsing_math_expression import parse_math_expression
from infix_to_postfix import infix_to_postfix, calculate_postfix_expression
from check_validity import check_var_name, check_variables


class SmartCalculator:
    commands = ('/exit', '/help')
    help_text = "The program calculates the result of an expression."
    variables = {}

    def handle_command(self, command):
        if command not in self.commands:
            print("Unknown command")
            return None

        if command == '/exit':
            print("Bye!")
            quit()

        if command == '/help':
            print(self.help_text)
            return None

    def assignment(self, equation):
        if '=' not in equation:
            return "Invalid assignment"

        operators = [operator.strip() for operator in equation.split('=', 1)]

        if check_var_name(operators[0]):
            print("Invalid identifier")
            return "Invalid identifier"

        assigned_value = parse_math_expression(operators[1])

        if not assigned_value:
            print("Invalid assignment")
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
        express = parse_math_expression(express)

        if not express:
            return "Invalid expression"

        express = check_variables(express, SmartCalculator.variables)

        if express == "Unknown variable":
            return "Unknown variable"

        if express == "Invalid identifier":
            return "Invalid identifier"

        postfix_express = infix_to_postfix(express)

        return str(calculate_postfix_expression(postfix_express))

    def dict_to_string(self, dicts):
        var_string = ''
        for key, value in dicts.items():
            var_string += f'{key} = {value}\n'

        return var_string

    def main(self):
        while True:
            tokens = input().strip()

            if not tokens:
                continue

            if tokens.startswith('/'):
                self.handle_command(tokens)
                continue

            if '=' in tokens:
                self.assignment(tokens)
                continue

            self.handle_expression(tokens)
