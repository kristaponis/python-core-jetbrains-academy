# Use the command and absolute mode to set permissions to read, write
# and execute the /tmp/test.exe file for all the users.
'''
$ chmod 777 /tmp/test.exe
'''


# You have a project file called /tmp/program.py. Your task is to make
# this file executable for other users.
'''
$ chmod o+x /tmp/program.py
'''


# Jim has to change the owner and the group of a test.txt file.
# The new owner is admin, and the new group is team.
# Which variant of the command below will help him with this task?
'''
$ chown admin:team ./test.txt
'''


# Nick wants to modify group permissions to a program.exe file so that
# the group members can read, write and execute it.
# Which variant of the command should he use?
'''
$ chmod g=rwx program.exe
'''
