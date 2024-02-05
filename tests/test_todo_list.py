# As a user
# So that I can keep track of my tasks
# I want to check if a text includes the string `#TODO`.

'''
check 

def check_todo(text):
    param = (text)
    text: string containing multiple things including ideally '#TODO'
    
    return:
        string if it contains '#TODO'
    
    side effects:
        if there isn't any '#TODO' it would return error saying there's no tasks
'''
pass    
        

from lib.todo_list import check_todo
import pytest    


'''
test to see if the text has no content
'''

def test_check_no_content():
    
    with pytest.raises(Exception) as err:
        outcome = check_todo('')
    error = str(err.value)
    assert error == 'No #TODO tasks'


'''
check if the text contains '#TODO'
'''

def test_check_todo():
    tasks = check_todo('testing to see if #TODO is detected')
    assert tasks == 'testing to see if #TODO is detected'

'''
check for the absence of #TODO
'''

def test_check_lack_of_todo():
    
    with pytest.raises(Exception) as err:
        no_tasks = check_todo('testing to see if this works')
    error_msg = str(err.value)
    assert error_msg == 'No #TODO tasks'


'''
check for #TODO but not necesarily in capitals
'''

def test_todos_in_lowerc():
    todos = check_todo('testing to see if #toDo works')
    assert todos == 'testing to see if #toDo works'