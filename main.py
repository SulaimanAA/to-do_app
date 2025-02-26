# Todo List

while True:

    user_action = input("Type add/show/edit/complete/exit: ")
    user_action = user_action.strip()

    match user_action:

        case 'add' | 'ADD' | 'Add':

            todo = input("Enter a todo: ") + "\n"


            with open('to-do_app/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('to-do_app/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'SHOW' | 'Show':

            with open('to-do_app/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = []
        
            for index, item in enumerate(todos): # enumerate(...) adds index number before each printed result of a list
                item = item.capitalize()
                item = item.strip('\n')

                row = f"{index + 1}- {item}"
                print(row)

        case 'edit' | 'EDIT' | 'Edit':

            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('to-do_app/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('to-do_app/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':

            number = int(input("Number of the todo to complete: "))

            with open('to-do_app/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('to-do_app/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case 'exit' | 'EXIT' | 'Exit':

            break

        case _: 

            print("Unknown command")


print("End")




# import builtins > print(dir(builtins)) -- import and list all the built in functions in python
# print(help([x].[method function])) gives brief description of what happens when method function is applied
# print(dir(str)) or print(dir("...")) to find all method functions such as ".append" or ".capitalize"




