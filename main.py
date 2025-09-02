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
"""
# Ask the user for their ideas, make it ask until there is a break
loop = True
while loop:
    idea = input("What sewing project would you like to add to your list? (if none type 'n')")

    if idea.lower() == "n":
        # read back the file to the user
        with open("projects.txt", "r") as r_file:
            print( f"Your list consists of: \n{r_file.read()}")
        loop = False

    else:
        # create if non-existent a new file, if it already exists.
        with open("projects.txt", "a") as file:
            file.write(idea + "\n")

        # read back the file to the user
        with open("projects.txt", "r") as r_file:
            print(r_file.read())

#Todo: Handle what happens when typing n if there is no existing file