#declare a variable
f = 0;
f1 = 1;
print f
print f1

#re-declaring a variable
f = "abc"
print f

#error: different types combined
#print "string type " + 123
print "string type " + str(123)

#global vs local variables in functions
def SomeFunction():
    global f
    f = "def"
    print f

SomeFunction()
print f

del f1
print f1
