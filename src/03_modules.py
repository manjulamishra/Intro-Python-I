"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
import sys
a = sys.argv[1]
b = sys.argv[2]
sum = a + b 
# print("sum of a and b is {}".format(int(a)+ int(b)))

# Print out the OS platform you're using:
print(sys.platform)

# Print out the version of Python you're using:
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

os.name
# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd()) # get current working directory
print(os.listdir(".")) # files in the current direcotry

# Print out your machine's login name
os.getusername()
# The above didn't work so I used the followinf import instead
import getpass
getpass.getuser()
