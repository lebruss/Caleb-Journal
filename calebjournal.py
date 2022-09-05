#caleb journal
from datetime import datetime#I use this to get the current time. Then I put this in the journal entry's file name
now = str(datetime.now())
now = now.replace(':', '')#remove : character from "now", because : ultimately cannot be used in Windows filenames
now = now.replace('/', '')
print("File name: " + now)
def SaveAndExit():#Save journal entry as a .txt file; Filename is current date and time; Filedirectory is the same as this python file
    f = open(now + ".txt", "w")#Open a .txt file: Today's date-time ("now" variable) .txt ; option "w" creates and opens this filename
    for line in journal:#For each "line" in the list of journal lines provided by the user,
        if line == "e" or line == "E":
            del line#E or e is intended as the user command to Save and Exit; remove these from the actual journal
        f.write(line)#write each line to this file
    f.close()


print("Caleb Journal--")
print("E for exit-----\n")

journal = []#a list, which contains each string line of the user's input
while True:
    line = str(input())#Each journal "line" is a user input, separated by Enter key
    journal.append(line)#Upon pressing Enter, add the user's journal "line" to the journal
    journal.append("\n")#Adds new line to each input
    if line == "e" or line == "E":#If user input is E or e , save and exit Calebjournal application
        SaveAndExit()
        break