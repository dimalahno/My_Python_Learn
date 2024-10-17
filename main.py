def get_todos(file_path="files/todos.txt"):
    """ Read a text file and returns the list of to-do items"""
    with open(file_path, "r") as f:
        return f.read().splitlines()

def save_todos(todos_args, file_path="files/todos.txt"):
    """ Write the to-do list to a file"""
    with open(file_path, "w") as f:
        f.write("\n".join(todos_args))

todos = get_todos()

while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        todos.append(todo)

        save_todos(todos)

    elif user_action.startswith("show"):

        for index, item in enumerate(todos):
            print(f"{index + 1}: {item.title()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:].strip())
            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo

            save_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[9:].strip())
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            save_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is not item with that number.")
            continue
    elif user_action.startswith("exit"):

        save_todos(todos)
        print("Bye!")
        break

    else:
        print("Command is not valid.")
