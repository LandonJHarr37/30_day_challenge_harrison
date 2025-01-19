import datetime

'''
Using a context manager and the write (to a file) function to create a personal diary with a date and time stamp
    after the entry

adjustments to make: format the time stamp/date and allow for user input (currently hardcoding one entry)

Author: Landon Harrison
Version: 1/19/2025
'''

#defining our own context management 
class Diary(object):
    def __init__ (self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__ (self):
        return self.file_obj
    def __exit__ (self, type, value, traceback):
        self.file_obj.close()

date_time = datetime.datetime.now()

with Diary("my_diary.txt", "w") as file:
    file.write("Day 1 (01/19/2025): This has been both an amazing and long day in Rome. \nI stook what 4 or 5 busses," \
               " and walked all over both trastevere and the Foro Romana (Roman Forum, I presume). \nI am so glad that I can be" \
                "comfortable even when I get lost!")

with Diary("my_diary.txt", "a") as file:    
    file.write(f" {date_time}")
    
with Diary("my_diary.txt", "r") as file:
        print(file.read())