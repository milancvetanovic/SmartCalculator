from parsing_math_expression import parse_math_expression
from infix_to_postfix import *


class SmartCalculator:
    commands = ('/exit', '/help')
    help_text = "The program calculates the result of an expression."
    variables = {}

    @staticmethod
    def var_name(name):
        if name.isalnum():
            if name[0].isdigit():
                return True
            else:
                return False
        else:
            return True

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
        operators = [operator.strip() for operator in equation.split('=', 1)]

        if self.var_name(operators[0]):
            print("Invalid identifier")
            return None

        assigned_value = parse_math_expression(operators[1])

        if not assigned_value:
            print("Invalid assignment")
            return None
        else:
            for i, item in enumerate(assigned_value):
                if item.isalnum():
                    if item.isnumeric():
                        continue
                    elif self.var_name(item):
                        print("Invalid identifier")
                        return None
                    else:
                        try:
                            assigned_value[i] = self.variables[item]
                        except KeyError:
                            print("Unknown variable")
                            return None

        assigned_value = infix_to_postfix(assigned_value)
        self.variables[operators[0]] = calculate_postfix_expression(assigned_value)
        return None

        # try:
        #     self.variables[operators[0]] = int(operators[1])
        # except ValueError:
        #     try:
        #         self.variables[operators[0]] = self.variables[operators[1]]
        #     except KeyError:
        #         if self.var_name(operators[1]):
        #             print("Invalid assignment")
        #             return None
        #         elif operators[1] not in self.variables:
        #             print("Unknown variable")
        #             return None

    def handle_expression(self, express):
        express = parse_math_expression(express)

        if not express:
            print("Invalid expression")
            return None
        else:
            for i, item in enumerate(express):
                if item.isalnum():
                    if item.isnumeric():
                        continue
                    elif self.var_name(item):
                        print("Invalid identifier")
                        return None
                    else:
                        try:
                            express[i] = self.variables[item]
                        except KeyError:
                            print("Unknown variable")
                            return None

        postfix_express = infix_to_postfix(express)
        print(calculate_postfix_expression(postfix_express))

        return None

    def main(self):
        while True:
            tokens = input().strip()

            if tokens.startswith('/'):
                self.handle_command(tokens)
                continue

            if '=' in tokens:
                self.assignment(tokens)
                continue

            self.handle_expression(tokens)
