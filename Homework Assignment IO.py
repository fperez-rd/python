"""

programmer: Felix Perez

Homework Assignment #8: Input and Output (I/O):

    Create a note-taking program. When a user starts it up, it should prompt them for a filename.

    If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After 
    they enter the text, it should save the file and exit.

    If they enter a file name that already exists, it should ask the user if they want:

    A) Read the file

    B) Delete the file and start over

    C) Append the file

    If the user wants to read the file it should simply show the contents of the file on the screen.
    
    If the user wants to start over then the file should be deleted and another empty one made in its place.
    
    If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 

    *Allow the user to select a 4th option:

    D) Replace a single line

    If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:

    1) The line number they want to update.

    2) The text that should replace that line.

"""

import os #library to verify if the filename exists.

FileName = input("Please enter the name of file: ")

if os.path.isfile(FileName):
    print("The filename",FileName,"already exist, please Enter the menu opcion: \n A) Read the file \n B) Delete the file and start over \n C) Append the file \n D) Replace a single line")
    MenuOptions = input()
    MenuOptions = MenuOptions.upper()

    if "A" in MenuOptions:
        Notes = open(FileName,"r")
        for line in Notes:
            print(line,end="")
        Notes.close()
    elif "B" in MenuOptions:
        Notes = open(FileName,"w")
        print("Enter your text to save in file override",FileName,":\n")
        TempNotes = input()
        Notes.write(TempNotes)
        Notes.close()
    elif "C" in MenuOptions:
        Notes = open(FileName,"r")
        for line in Notes:
            print(line,end="")
        Notes.close()
        Notes = open(FileName,"a")
        print("\nContinue writing the text from file",FileName,":")
        TempNotes = input()
        Notes.write("\n")
        Notes.write(TempNotes)
        Notes.close()
    elif "D" in MenuOptions:

        Notes = open(FileName,"r")
        for line in Notes:
            print(line,end="")
        print("\n")
        Notes.close()

        LineToReplace = int(input("Select number line to replace: "))
        TextToReplace = input("Input text to replace the line: ")

        Notes = open(FileName,"r")

        TempNotes = Notes.read().splitlines()

        Notes.seek(0,0)

        NewNotes = ""
        for line in Notes:
            LineStrip = line.strip()
            LineNew = LineStrip.replace(TempNotes[LineToReplace-1],TextToReplace)
            NewNotes += LineNew+"\n"
        Notes.close()
        Notes = open(FileName,"w")
        Notes.write(NewNotes)
        Notes.close()
    else:
        print("Option is not correct, bye!")

else:
    Notes = open(FileName,"w")
    print("Enter your text to save in file",FileName,":\n")
    TempNotes = input()
    Notes.write(TempNotes)
    Notes.close()