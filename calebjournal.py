#caleb journal
from datetime import datetime#I use this to get the current time. Then I put this in the journal entry's file name
now = datetime.now()
filename = now.strftime("%d/%m%Y %H%M%S")
filename.replace(':', '')#remove : character from "now", because : ultimately cannot be used in Windows filenames
filename.replace('/', '')#remove : character from "now", because : ultimately cannot be used in Windows filenames
print(str(filename))
filename = "today"#Change this to get the filename correct with today's date and time
def save():#Save journal entry as a .txt file; Filename is current date and time; Filedirectory is the same as this python file
    f = open(filename + ".txt", "w")
    for line in line_list:#For each "line" in the list of journal lines provided by the user,
        f.write(line)#write each line to this file
    f.close()


print("Caleb Journal--")
print("E for exit-----\n")

line_list = []#a list, which contains each string line of the user's input
while True:
    line = str(input())
    line_list.append(line)
    line_list.append("\n")
    if line == "e":
        #for line in line_list:
            #print(line)
        save()
        break
    if line == "E":
        save()
        break
