# Todo List
# from functions import get_todos, write_todos (Can use this instead of (see below (line 3)))
import functions
import time

now = time.strftime("%b %d %Y - %d/%m/%Y - %H:%M:%S")
print("Date - Time:", now)

while True:

    user_action = input("Type add/show/edit/complete/exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        new_todos = []
    
        for index, item in enumerate(todos): # enumerate(...) adds index number before each printed result of a list
            item = item.capitalize()
            item = item.strip('\n')

            row = f"{index + 1}- {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):

        break

    else:
        print("Command Invalid")

print("End")




# import builtins > print(dir(builtins)) -- import and list all the built in functions in python
# print(help([x].[method function])) gives brief description of what happens when method function is applied
# print(dir(str)) or print(dir("...")) to find all method functions such as ".append" or ".capitalize"




