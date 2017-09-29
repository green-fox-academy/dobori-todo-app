import sys



class Todo_controller(object):
    index = ""

    def __init__(self):
        if len(sys.argv) == 2 and sys.argv[1] == "-l":
            return self.todo_list_read()
        elif len(sys.argv) == 2 and sys.argv[1] == "-a":
            return self.add_todo()
        elif len(sys.argv) == 2 and sys.argv[1] == "-r":
            return self.delete_line()
        elif len(sys.argv) == 2 and sys.argv[1] == "-c":
            return self.todo_list_check()
        elif len(sys.argv) == 1:
            print("Command Line Todo application")
            print("=============================")
            print("Command line arguments:")
            print(" -l   Lists all the tasks")
            print(" -a   Adds a new task")
            print(" -r   Removes an task")
            print(" -c   Completes an task")
        elif len(sys.argv) == 3 and sys.argv[1] == "-a":
            self.index = str(sys.argv[2])
            return self.add_todo(self.index)
        elif len(sys.argv) == 3 and sys.argv[1] == "-r":
            self.index = int(sys.argv[2])
            return self.delete_line(self.index)
        elif len(sys.argv) == 3 and sys.argv[1] == "-c":
            self.index = int(sys.argv[2])
            return self.todo_list_check(self.index)

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


    def add_todo(self, index):
        todo_input = self.index
        self.textfile = open("todo_list.txt", "a")
        self.textfile.write("0 " + todo_input + "\n")
        self.textfile.close()

    def delete_line(self, index):
        self.textfile = open("todo_list.txt", "r")
        lines = self.textfile.readlines()
        self.textfile.close()
        newlines = ""
        for i in range(len(lines)):
            if i == int(self.index)-1:
                del lines[int(self.index)-1]
            self.newlines = "".join(lines)
        self.write_todotxt(self.newlines)

    def todo_list_check(self, index):
        self.textfile = open("todo_list.txt", "r")
        lines = self.textfile.readlines()
        self.textfile.close()
        for i in range(len(lines)):
            if int(check_input) == i:
                lines[i][:1].replace('0', '1')
        newlines = "".join(lines)
        self.write_todotxt(self.newlines)

    def write_todotxt(self, newlines):
        self.textfile = open("todo_list.txt", "w")
        self.textfile.write(self.newlines)
        self.textfile.close()  



todo = Todo_controller()   



