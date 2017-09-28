import sys


dict_item = {}


class Todo_controller(object):
    

    def __init__(self):
        if len(sys.argv) == 2 and sys.argv[1] == "-l":
            return self.todo_list_read()
        elif len(sys.argv) == 2 and sys.argv[1] == "-a":
            return self.add_todo()
        elif len(sys.argv) == 2 and sys.argv[1] == "-r":
            print("removeolj")
        elif len(sys.argv) == 2 and sys.argv[1] == "-c":
            print("check")
        elif len(sys.argv) == 1:
            print("Command Line Todo application")
            print("=============================")
            print("Command line arguments:")
            print(" -l   Lists all the tasks")
            print(" -a   Adds a new task")
            print(" -r   Removes an task")
            print(" -c   Completes an task")
        

    def todo_list_read(self):
        self.todo_elements = open("todo_list.txt", "r")
        todo_list = self.todo_elements.read()
        print(todo_list)
        self.todo_elements.close()


    def add_todo(self):
        todo_input = input(str("Please write a new task: "))
        self.textfile = open("todo_list.txt", "a")
        self.textfile.write("0 " + todo_input + "\n")
        self.textfile.close()





todo = Todo_controller()   



