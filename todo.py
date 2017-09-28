import sys


dict_item = {}


class Todo_controller(object):
    

    def __init__(self):
        if len(sys.argv) == 2 and sys.argv[1] == "-l":
            print("listazz")
        elif len(sys.argv) == 2 and sys.argv[1] == "-a":
            print("adj hozza ujat")
        elif len(sys.argv) == 2 and sys.argv[1] == "-r":
            print("removeolj")
        elif len(sys.argv) == 2 and sys.argv[1] == "-c":
            print("check")
        elif len(sys.argv) == 1:
            print("menut irasd ki")
        

    def todo_list_read(self, file_read):
        self.todo_elements = self.file_read
        self.todo_list = self.todo_elements.read()
        print(self.todo_list)
        self.todo_elements.close()

    def add_todo(self, todo_input):
        textfile = open("todo_list.txt", "w")
        textfile.write("0 " + todo_input + "\n")
        textfile.close()

file_read = open("todo_list.txt", "r")
file_write = open("todo_list.txt", "w")


todo = Todo_controller()
todo.add_todo("walking dead")    



