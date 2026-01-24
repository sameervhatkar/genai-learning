# file = open("log.txt", 'w')
# file.write("Day 2 Learning File and Operating System.")
# file.close()

# file = open("log.txt", 'a')
# file.write("Appending new Line.")
# file.close()

# file = open("log.txt", 'r')
# content = file.read()
# file.close()
# print(content)

# with open("log.txt", 'w') as file:
#     file.write("Day 2 Learning File and Operating System\n")

# with open("log.txt", 'a') as file:
#     file.write("Appending new line\n")


import os
from datetime import date

# print(os.getcwd())

# os.mkdir("ai_logs")


answer = input("What did you learn today? ")
with open("ai_logs/activity.txt", 'a') as file:
    file.write(f"{date.today()} - {answer}\n")
    



