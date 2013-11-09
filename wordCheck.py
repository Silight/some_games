# A simple error check to make sure the user entered a word. 

original = raw_input("What would you like to convert? ")
if len(original) > 0:
    print original
else:
    print "empty"
