history = []

def add_entry(command_name, a, b, result):
    entry = {'Operation': command_name, 'Operand1': str(a), 'Operand2': str(b), 'Result': str(result)}
    history.append(entry)
    "history.append((operation, a, b, result))"

def get_history():
    return history
