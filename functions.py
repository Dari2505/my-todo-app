FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of 
    todo items.
    """                                       # by giving a value to the argument:filepath="files/todos.txt", we don't have to
    with open(filepath, 'r') as file_local:   # type something like: todos = get_todos("files/todos.txt")
        todos_local = file_local.readlines()  # instead we write todos = get_todos()

    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file  """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


 #This block of code, makes it possible that what is indented will only be executed when this python file (functions.py)
 # is executed, not when other python files, which import this module are executed
print(__name__)
if __name__=="__main__":
    print("Hello from functions")
    print(get_todos())