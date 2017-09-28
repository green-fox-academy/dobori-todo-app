import sys

#how to ues arguments
#print("This is the name of the script: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: " , str(sys.argv))

#for x in sys.argv:
#   print "Argument: ", x

file_read = open("todo_list.txt", "r")
file_write = open("todo_list.txt", "w")

list_of_todo = []
dict_item = {}


class Todo_controller(object):

    def todo_list_read(self, file_read):
        self.todo_elements = self.file_read
        self.todo_list = self.todo_elements.read()
        print(self.todo_list)
        self.todo_elements.close()


    def make_list(self):
        todo_input = "walking dead"
        self.dict_item['ready_or_not'] = False
        self.dict_item['name'] = todo_input
        self.list_of_todo.append(dict_item)
        self.add_todo(list_of_todo)
        return(list_of_todo)
    

    def add_todo(self, file_write):
        self.todo_elements = self.file_write
        self.todo_list = self.todo_elements.write()
        self.
        return(list_of_todo)


