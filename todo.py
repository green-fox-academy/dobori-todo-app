import sys


dict_item = {}


class Todo_controller(object):
    

    def __init__(self):
        if len(sys.argv) == 2 and sys.argv[1] == "-l":
            return self.todo_list_read()
        elif len(sys.argv) == 2 and sys.argv[1] == "-a":
            return self.add_todo()
        elif len(sys.argv) == 2 and sys.argv[1] == "-r":
            return self.delete_line()
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
        i = 0
        for line in self.todo_elements.readlines():
            i += 1
            splitted_line = line.split() 
            if splitted_line[0] == "0":
                splitted_line[0] = "[ ]"
            else:
                splitted_line[0] = "[X]"
            newline = " ".join(splitted_line)
            print(str(i) + " - " + newline)

        self.todo_elements.close()


    def add_todo(self):
        todo_input = input(str("Please write a new task: "))
        self.textfile = open("todo_list.txt", "a")
        self.textfile.write("0 " + todo_input + "\n")
        self.textfile.close()

    def delete_line(self):
        delete_input = input("Please write which line do you want to remove: ")
        self.textfile = open("todo_list.txt", "r")
        lines = self.textfile.readlines()
        self.textfile.close()

        for i in range(len(lines)):
            if i == int(delete_input)-1:
                del lines[int(delete_input)-1]
            newlines = "".join(lines)
        self.textfile = open("todo_list.txt", "w")
        self.textfile.write(newlines)
        self.textfile.close()
        



todo = Todo_controller()   



