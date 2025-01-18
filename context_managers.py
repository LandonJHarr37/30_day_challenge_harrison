'''
Context managers to open, read, and close files; file management; 

Author: Landon Harrison
Version: 1/18/2025
'''

#a context manager differs from usual file management because it handles closing for you and has a cleaner structure
#   smarter way to manage resources (Oren Cohen)

#defining our own context management 
class File(object):
    def __init__ (self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__ (self):
        return self.file_obj
    def __exit__ (self, type, value, traceback):
        self.file_obj.close()

#writing to text_context_manage.txt using a write with statment
with File("text_context_manage.txt", "w") as file:
    file.write("\nMy name is Landon and I am practicing file management using a context manager.\n")

#reading the text_context_manage.txt file to the terminal using a context manager
with File("text_context_manage.txt", "r") as file:
    print(file.read())

#appending a message
with File("text_context_manage.txt", "a") as file:
    file.write("\nI am sitting with my flatemate in Italy and writing code.")

with File("text_context_manage.txt", "r") as file:
    print(file.read())


