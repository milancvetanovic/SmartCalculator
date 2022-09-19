class SmartCalculator:
    commands = ('/exit', '/help')
    help_text = "The program calculates the result of an expression."
    variables = {}

    @staticmethod
    def var_name(name):
        return not name.isalpha()

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

        try:
            self.variables[operators[0]] = int(operators[1])
        except ValueError:
            try:
                self.variables[operators[0]] = self.variables[operators[1]]
            except KeyError:
                if self.var_name(operators[1]):
                    print("Invalid assignment")
                    return None
                elif operators[1] not in self.variables:
                    print("Unknown variable")
                    return None

    def handle_expression(self, expression):
        operators = expression.split()

        if len(operators) == 1:
            try:
                print(int(operators[0]))
                return None
            except ValueError:
                try:
                    print(self.variables[operators[0]])
                    return None
                except KeyError:
                    if self.var_name(operators[0]):
                        print("Invalid identifier")
                        return None
                    else:
                        print("Unknown variable")
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
