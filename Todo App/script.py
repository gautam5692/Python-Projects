import json

print("Todo List...")

print("Type 'list' for listing all your todos.")
print("Type 'add' to add a todo.")
print("Type 'modify <todo_number>' to modify a todo.")
print("Type 'delete <todo_number>' to delete a todo.")
print("Type 'exit' to exit the command line.")

try:
  with open("todo.json", "r") as todo_file:
    todo_list = json.load(todo_file)
except FileNotFoundError:
  todo_list = []

def update_todo(todo_task, todo_date):
  todo_list.append({"todo_task": todo_task, "todo_date": todo_date})

def write_into_file():
  with open("todo.json", "w") as todo_file:
    json.dump(todo_list, todo_file)

while True:

  command = input("Enter the command you want: ")

  if len(command.split()) == 1:
    match command.lower():
      case "list":
        if len(todo_list) != 0:
          for index, item in enumerate(todo_list):
            print(f"{index+1}. todo_task: {item["todo_task"]}, todo_date: {item["todo_date"]}")
        else:
          print("There is no todo.")
      
      case "add":
        todo_task = input("Enter the todo_task: ")
        todo_date = input("Enter the todo_date: ")
        update_todo(todo_task, todo_date)
        write_into_file()

      case "exit":
        break

      case _:
        print("Invalid Input")
        
      
  elif len(command.split()) == 2:
    command_as_list = command.split()
    try:
      list_index = int(command_as_list[1]) - 1
    except ValueError:
      print("List index has to be a number")
      continue
    match command_as_list[0].lower():
      case "modify":
        try:
          print(f"Current status of todo_no {list_index + 1}: ")
          print(todo_list[list_index])
          print("If you want to cancel the modification, simply type 'no_change'.")
          modify_task = input("Modify the task here: ")
          modify_date = input("Modify the date here: ")
          if modify_task != "no_change":
            todo_list[list_index]["todo_task"] = modify_task
          else:
            pass

          if modify_date != "no_change":
            todo_list[list_index]["todo_date"] = modify_date
          else:
            pass

          write_into_file()

        except IndexError:
          print(f"There is no todo numbered as {list_index + 1}")
      
      case "delete":
        try:
          todo_list.pop(list_index)
        except IndexError:
          print(f"There is no todo numbered as {list_index + 1}")
        write_into_file()

      case _:
        print("Invalid command.")

