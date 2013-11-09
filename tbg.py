# tbg - Text-Based Game, I was building it when I got bored writing my novel. I had just played Zork for the first time. This is also a work in progress. And buggy as hell. 

from sys import argv

script, user_name = argv
prompt = ('> ')

def charater_type_select(): # Allows user to select a character type
    while True:
        if userType = thief:
            thief = userType
        elif userType = warrior:
            warrior = userType
        elif userType = mage
            mage = userType
        else:
            print "That is not a valid character type."
        return userType

# Main game loop
while True:
    print "Welcome %r to our little dragon adventure." % user_name
    print """
    You are an adventurer looking for treasure.
    What kind of adventurer are you? (thief, warrior, mage)
    """
    userType = raw_input(prompt)
    character_type_select()

    print """
    Well, %r you have just finished your %r training and 
    you found your first job.

    You are supposed to enter one of the caves
    in front of you and retrieve the treasure
    rumored to lie within.
    """ % (user_name, userType)


