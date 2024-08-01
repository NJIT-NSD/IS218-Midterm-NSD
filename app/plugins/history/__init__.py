from app.commands import Command
from utils.history import get_history

class HistoryCommand(Command):
    def execute(self):
        history = get_history()
        if not history:
            print("No history available.")
        else:
            for operation, a, b, result in history:
                print(f"{operation} {a} {b} = {result}")
