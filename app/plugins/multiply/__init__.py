from app.commands import Command
from decimal import Decimal, InvalidOperation
import logging
import logging.config
from utils.history import add_entry

class MultiplyCommand(Command):
    def execute(self, a, b):
        try:
            a = Decimal(a)
            b = Decimal(b)
            result = a * b
            add_entry('multiply', a, b, result)
            logging.info(f"operation = multiply variables = {a}, {b} result = {result}")
            print(f"The result of {a} * {b} is {result}")
        except InvalidOperation:
            logging.error(f"Invalid Number Input Error")
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except Exception as e:
            logging.error(f"Exception Made")
            print(f"An error occurred: {e}")