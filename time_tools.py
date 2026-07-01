from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%A, %d %B %Y | %I:%M:%S %p")