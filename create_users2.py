#!/usr/bin/python3

# INET4031
# Sai Yang
# 03/25/2025
# 03/25/2025

#The os module allows for the code to handle cwd, mkdir, ls, rmdir.
#The re module allows for the code to use regular expression such as findall, search, split, and sub
#The sys module allows for the interpreter to provides access to the variables and functions
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():

    #If the user types in 'Y', dry run will execute, if 'N' is the os command will add the user to the system.
    user_input = input("Press 'Y' for dry-run or 'N' to run code normally\n")
    #read the input file that includes the user data.
    with open('create_users.input', 'r') as file:
        for line in file:

        #This regular expression is looking for '#' to make sure that it is not reading any of the comments.
            match = re.match("^#",line)

        #line.strip removes any trailing whitespaces or newline characters.
            fields = line.strip().split(':')

        #This if statement runs through each rows of the input file. If the values in each rows has more than 5 fields, it will stop. If not it will continue running. If it has 5 fields then there is no need to modify the field. The if statement will print out that the line does not have enough field if there are less than 5 fields. If there is a # at the front of a value, it will print that it skipped that line.
            print("test")
            if match or len(fields) != 5:
                if user_input == 'Y':
                    if len(fields) !=5:
                        print("Line does not have enough fields")
                    if match:
                        print("Line was skipped")
                continue

        #These three lines set the variables: username, password, and gecos, to the values corresponding to the indexes of the values in the open file.
            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3],fields[2])

        #split in this line uses ',' as a delimiter to separate the group field into a list
            groups = fields[4].split(',')

        #this print statement verifies that the 'username' is being created. It is sort of like a test to make sure the code is running.
            print("==> Creating account for %s..." % (username))
        #this os command is adding users to the system. it disables password for the user initially and using gecos, it shows the user's information
            cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #if the user wants to dry run 'Y' it will type in dry running, if not then the os command will execute and add the users virtually.
            if user_input == 'Y':
                print("Dry running test")
            else:
                os.system(cmd)
        #This print statement checks to see the creation of the password. It is testing to make sure the code is working.
            print("==> Setting the password for %s..." % (username))
        #this command is setting a password for a username. The password must not have trailing newline (-ne), special characters(-e), and a new line(\n). It will ask for the password to be typed twice for confirmation (%s\n%s).
            cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd will run the cmd string "/bin/echo -ne......... as if it was to be run in the terminal. If the user want to dry run it will dry run, if not the os commmand will execute and add the users to the system
            if user_input == 'Y':
                print("dry running test 1")
            else:
                os.system(cmd)

            for group in groups:
            #this for loop will assign the user to the groups to it's corresponding group. It does this by using the os command to run the 'cmd' string to have access to assign the group. If the groups is = '-' then it will skip it. the dry running test will print that it is running if the user typed in 'Y'. 
                if group != '-':
                    print("==> Assigning %s to the %s group..." % (username,group))
                    cmd = "/usr/sbin/adduser %s %s" % (username,group)
                    if user_input == 'Y':
                        print("dry running test 2")
                    else:
                        os.system(cmd)

if __name__ == '__main__':
    main()
