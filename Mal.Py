# This is the main file of the Mal.Py repository and program on GitHub. ("https://github.com/Eli-Sterken/Mal.Py") Please read the README.md and LICENSE files on this repository first.

# First, we import the required extentions

import time, os, shutil, zipfile, platform

# Next, we set the required varibles

Current_Directory = os.getcwd()
Verson = "1.0.0"
Repository_URL = "https://github.com/Eli-Sterken/Mal.Py"
Sample_Number = 0
System_Type = platform.system()

# now, we create a folder to keep the ziped files before we extract them

if (System_Type == "Windows"):
    os.system('mkdir C:\Windows\Temp\Mal.Py')
    os.system('mkdir C:\Windows\Temp\Mal.Py\"Zip_Holding"')
elif ("1" == "1"):
    os.system('mkdir /usr/bin/Temp')
    os.system('mkdir /usr/bin/Temp/Mal.Py')
    os.system('mkdir /usr/bin/Temp/Mal.Py/"Zip_Holding"')

Main_Input = input(f"Welcome to Mal.Py! This program is disigned to help you download and run malware for research purposes. Please read the license and readme files at {Repository_URL} before continuing. I am not responsible for any damage caused by downloading malware. \n"
                   "\n"
                   "Press 'C + Enter' to close \n"
                   "\n" 
                   "Press 'V + Enter' for verson info \n"
                   "\n"
                   "Press 'R + Enter' to run malware and select analasys tools \n"
                   "\n"
                   "Press 'D + Enter' to download malware samples \n"
                   "\n"
                   "Press 'S + Enter' to save malware in a safe format \n") # Asks the user what they want to do, and tells them about aditonal info and the desclamer.
if (Main_Input == "V") or (Main_Input == "v"): # If the user inputs "V" for verson info
    print(f"Mal.Py verson {Verson}") # Print the verson
    print("Made with love by Eli Sterken! :)") # Print the made with love message
    print(f"More info at {Repository_URL}") # Print the more info message
    Will_Close_1 = input("Press 'C + Enter' to close the program") # Ask the user if they want to close the program
    if (Will_Close_1 == "C") or (Will_Close_1 == "c"):
        quit() # If the user inputs "C", close the program
    elif ("1" == "1"):
        print("Invalid input, closing in 5 seconds.") # If the input is invalid, print so and close in 5 seconds
        time.sleep(5)
        quit() # Close the program
elif (Main_Input == "C") or (Main_Input == "c"): # If the user inputs "C"
    quit() # Close the program        
elif (Main_Input == "D") or (Main_Input == "d"): # If the user presses "D" to download malware
    Download_Warning = input("Warning, you are about to download bare malware exe files. To continue, press 'Y + Enter', or to close the program, press 'C + Enter'.") # Lets the user know about the dangers
    if (Download_Warning == "C") or (Download_Warning == "c"):
        quit() # If the user inputs "C", close the program
    elif (Download_Warning == "Y") or (Download_Warning == "y"): # If the user inputs "Y" to download malware
        Directory_Question = input("Please type a path to a directory where you would like to save the malware files") # Ask the user to type a path where they would like to save the malware
        if (os.path.exists(Directory_Question)): # Test if the path the user inputed is valid
            print(f"Your operating system is: {System_Type}")
            time.sleep(5)
        elif ("1" == "1"): # If it is not
           Will_Close_1 = input("Invalid path, press 'C + Enter' to close the program") # Ask the user if they want to close the program
           if (Will_Close_1 == "C") or (Will_Close_1 == "c"):
               quit() # If the user inputs "C", close the program
           elif ("1" == "1"):
               print("Invalid input, closing in 5 seconds.") # If the input is invalid, print so and close in 5 seconds
               time.sleep(5)
               quit() # Close the program     
    elif ("1" == "1"):
        print("Invalid input, closing in 5 seconds.") # If the input is invalid, print so and close in 5 seconds
        time.sleep(5)
        quit() # Close the program  

    



