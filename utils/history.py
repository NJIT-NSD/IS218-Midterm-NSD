history = []

def add_entry(operation, a, b, result):
    history.append((operation, a, b, result))

def get_history():
    return history
