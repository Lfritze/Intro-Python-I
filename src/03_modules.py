"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
  print(arg)

  for arg in sys.argv:
    print(f"Argument {arg}")

# Print out the OS platform you're using:
# YOUR CODE HERE
import platform
print("I am on " + sys.platform + " OS.")

print(f"You are on {platform.system()}")

# Print out the version of Python you're using:
# YOUR CODE HERE

print ("You are using Python version", str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]) + ".")

version_full = f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} Release -- {sys.version_info[3]}"
print(f"I am using Python version {version_full}")

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"Process ID: {os.getpid()}")
print("The process ID is:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

print(f"The CWD is: {os.getcwd()}")
print("Current working directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(f"Machine Login Name: {os.getlogin()}")
print("Machine Login name again!:", os.getlogin())