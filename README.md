## INET4031 Add Users Script and User List

## Program Description

# This automated script is able to add users atomatically without having to manually added them yourself. Usually to add users, the user would have to manually type in sudo adduser user02 and assign a group to it if needed. This automated system reads a user input text row by row and adds the user to the system

## Program User Operation

# This program takes in a file on the command line and adds users to the system. It does this by cleanly reading the values in the input file by. This makes sure the program is reading the values correctly. By reading each value and ensuring that it's valid, the value will be added to the system with its value corresponding to its field. 

# Input File Format

### The input file is formatted into 5 fields separated by a ':'. The first field is user, second is password, thrid is lastname, fourth is firstname, and fifth is group. If the user does not include enough field, this system will utilize an 'if' statement and skip it. If the user does not want to add a user to any group, they can input '-' in the group field.

# Command Execuction

### This program uses 3 modules, os, sys, and re to execute. To execute this program, you would need to utilize a function in the sys module called sys.stdin. This allows for the command line to take in a prompt, which in this case is create_users.input. On the command line, you would need to set the file to executable by typing in 'chmod +x <filename>. After doing so, you can type in './create-users.py < createusers.input' to execute it.

# "Dry Run"

### The create_users2.py file gives the user the choice to execute a dry run or a normal run. A dry run executes the file but does not actually add the users to the system. Instead, it prints out if it succeeds or not and will print out print statements if there are errors in the user fields. A normal run executes the os cmd and will add the users to the system.
