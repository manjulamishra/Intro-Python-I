"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# One way to open it
f = open('foo.txt')
print (f.read())

# More preferred way to open a file
with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)
f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# Writing a .txt file
f = open('bar.txt', 'w')
f.write( 'This is a testfile.\nI like to write.\nthis is amazing')
f.close()

# reading the file I just wrote
with open('bar.txt') as f:
    read_data = f.read()
    print(read_data)
f.closed