"""
13. File Handling (read/write files)
What you should know: Save and load data from text files.
 Practice Prompt: Write a program that saves your current sewing project ideas to a
 file called projects.txt, then reads it back to display.
"""


"""--------------------Initial Code------------------------------"""
# # Ask the user for their ideas, make it ask until there is a break
# loop = True
# while loop:
#     idea = input("What sewing project would you like to add to your list? (if none type 'n')")
#
#     if idea == "n" or idea == "N":
#         # read back the file to the user
#         r_file = open("projects.txt", "r")
#         print( f"Your list consists of: {r_file.read()}")
#         loop = False
#
#     else:
#         # create if non-existent a new file, if it already exists, save it to the file.
#         file = open("projects.txt", "w")
#         file.writelines(idea)
#         file.close()
#         # read back the file to the user
#         r_file = open("projects.txt", "r")
#         print(r_file.read())

"""--------------------Improved Code------------------------------
---------notes--------------
*use idea.lower() instead of typing out "n" or "N"
* "a" creates the file if it doesn't exist and appends if the file does exist
* use with open(...) so you don’t have to manually close() every time
*use "if os.path.exists("projects.txt") instead of a try and except to avoid catching unnecessary exceptions 
"""
# import os
# # Ask the user for their ideas, make it ask until there is a break
# loop = True
# while loop:
#     idea = input("What sewing project would you like to add to your list? (if none type 'n')")
#
#     if idea.lower() == "n":
#         if os.path.exists("projects.txt"):
#             # read back the file to the user
#             with open("projects.txt", "r") as r_file:
#                 print( f"Your list consists of: \n{r_file.read()}")
#         else:
#             print("No projects saved yet.")
#
#         loop = False
#
#     else:
#         # create if non-existent a new file, if it already exists.
#         with open("projects.txt", "a") as file:
#             file.write(idea + "\n")
#
#         # read back the file to the user
#         with open("projects.txt", "r") as r_file:
#             print( f"Your list consists of: \n{r_file.read()}")
"""-----------------------------Final Code---------------------"""
"""#notes
*don't need to open projects.txt in two different places, make a function
*don't need unnecessary variable loop, when you can just write while true:/ break
*.strip() removes spaces, newlines and tabs
"""
import os
#read and display sewing projects list
def show_projects():
    if os.path.exists("projects.txt"):
        with open("projects.txt", "r") as r_file:
            content = r_file.read().strip()
            if content:
                print("\nYour project list consists of:\n" + content)
            else:
                print("\nYour project list is empty.")
    else:
        print("\n No projects saved yet.")

while True:
    idea = input("What sewing project would you like to add to your list? (if none type 'n')")

    if idea.lower() == "n":
        if os.path.exists("projects.txt"):
            show_projects()
            break
    else:
        # create if non-existent a new file, if it already exists.
        with open("projects.txt", "a") as file:
            file.write(idea + "\n")
        show_projects()
