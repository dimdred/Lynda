# open a file for writing and create it if it doesn`t exist
f = open("textfile.txt", "w+")

# write some lines of data
for i in range(10):
    f.write("This is line %d\r\n" %(i+1))

f.close()

# open the file for appending file

f = open("textfile.txt", "a+")

for i in range(10):
    f.write("This is line %d\r\n" %(i+11))

f.close()

# f = open("textfile.txt", "r")
# if f.mode == 'r':
#     contents = f.read()
#     print contents

# read the individual lines into a list
f = open("textfile.txt", "r")
fl = f.readlines()
for x in fl:
    print x