# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string `#TODO`.

def check_todo(text):
    if '#TODO' in text.upper():
        return text
    else:
        raise Exception('No #TODO tasks')