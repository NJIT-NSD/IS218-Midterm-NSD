from app.commands import Command
from decimal import Decimal, InvalidOperation
import logging
import logging.config

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            a = Decimal(a)
            b = Decimal(b)
            result = a / b
            logging.info(f"operation = divide variables = {a}, {b} result = {result}")
            print(f"The result of {a} / {b} is {result}")
        except ZeroDivisionError:
            logging.info(f"Division by Zero Error")
            print(f"Cannot divide by zero.")
        except InvalidOperation:
            logging.info(f"Invalid Number Input Error")
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")