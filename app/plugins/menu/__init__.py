from app.commands import Command
import logging
import logging.config

class MenuCommand(Command):
    def execute(self):
        logging.info(f"Menu Request")
        print(f'Menu: csv, data, greet, Add, Subtract, Multiply, Divide')