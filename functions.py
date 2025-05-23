FILEPATH = "to-do_app/todos.txt"


def get_todos(filepath = FILEPATH):
    """ Read text file
    Return list of to-do items """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()

    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ Write to-do item list in text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())