import sys
import os
import re

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

# The project Directory
top = str(sys.argv[1])

print os.pathsep

def return_temp_name(filename):
    explode = filename.split(".")
    temp_name = explode[0] + "." + "min" + "." + explode[1]
    return temp_name

def minimize(filename):
    min_file = open( os.path.join( root, return_temp_name(file)), "w")
    data = filename.read()
    data = re.sub(r"(\t|\s|\r|\n)", "", data) # Remove space, tabs, formfeeds, newlines.
    data = re.sub(r"(\/\/.*?$)|(\/\*.*?\*\/)", "", data) # Remove comments
    print data
    min_file.close()
    filename.close()

# Recursive Directory Traversal Mechanism
for root, dirs, files in os.walk( top, topdown=True, onerror=None, followlinks=False):
    print "Root: ", root
    #print "Directories: ", dirs
    for file in files:
        if file.endswith('.css'):
            print "CSS File: ", file
            print "Path: ", os.path.join( root, file)
            minimize(open( os.path.join( root, file), "r"))
        elif file.endswith('.js'):
            print "Javascript File: ", file
            print "Path: ", os.path.join( root, file)
            js_file = open( os.path.join( root, file), "r")
            min_file = open( os.path.join( root, return_temp_name(file)), "w")
            js_file.close()
            min_file.close()
        elif file.endswith('.html'):
            print "HTML File: ", file
            print "Path: ", os.path.join( root, file)
