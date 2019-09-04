######################################################################
# Author: Shawn Villahermosa
# Username: villahermosas
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1

import time
user_input = (input("What is your birth year?"))

# User inputs their birth years.
if user_input == "2000":
    print("Yooo! You're a Dragon!")
    time.sleep(2)
    print("And no you can't breathe fire...")
    print("... trust me, I've tried it.")

elif user_input == "2001":
    print("You're a sssneaky ssssneaky Sssnake! \n")
    time.sleep(2)
    print("What do you call a Mexican snake?")
    time.sleep(2)
    print("A hissspanic! Hahah!")

elif user_input == "2002":
    print("Hay! You're a Horse! \n")
    time.sleep(2)
    print("What do you call a horse that lives next door?")
    print("A neigh-bor!")

elif user_input == "2003":
    print("You have 'goat' to be kidding me! You're a Goat!")

elif user_input == "2004":
    print("You're a monkey! \n")
    time.sleep(2)
    print("Explains why you keep going bananas...")

elif user_input == "2005":
    print("According to the Chinese calendar, you are a Rooster! \n")
    print("You have just been egg-ucated!")

elif user_input == "2006":
    print("You're a Dog!")
    print("In a couple of days, you might just pug-get about it.")

elif user_input == "2007":
    print("You are a Pig! (No offense) \n")
    time.sleep(2)
    print("If you took offense to that, here's a little joke to maybe set things right: ")
    print("Why did the pig quit sunbathing? \n")
    time.sleep(3)
    print("Because he was bacon in the heat!")
    print("Hope that made you feel better!")

elif user_input == "2008":
    print("Squeak! You're a Mouse! \n")
    time.sleep(2)
    print("One time I had a rat in my house and gave it poison...")
    print("... it didn't die so I guess it was Ratsputin.")

elif user_input == "2009":
    print("You are an Ox! \n")
    time.sleep(2)
    print("I'm sorry I don't have any puns for oxen...")
    time.sleep(2)
    print("...or do I?")
    time.sleep(2)
    print("No I don't.")

elif user_input == "2010":
    print("You're a Tiger! \n")
    time.sleep(2)
    print("Why don't tigers like fast food?")
    time.sleep(2)
    print("Because they can't catch it!")

elif user_input == "2011":
    print("You're a Rabbit! \n")
    time.sleep(2)
    print("When you've been forgotten by someone...")
    print("...now you're just some bunny that they used to know...")

######################################################################
# (Required) Task 2
# Asks the user for their friend's birth years.

print("")

friend_user_input = (input("What is your friend's birth year?"))

# User inputs their friend's birth years.
if friend_user_input == "2000":
    print("Yooo! They're a Dragon like you!")
    print("How awesome is that?!")

elif friend_user_input == "2001":
    print("They're a snake!")

elif friend_user_input == "2002":
    print("They're a Horse!")

elif friend_user_input == "2003":
    print("They're a Goat!")

elif friend_user_input == "2004":
    print("They're a monkey!")

elif friend_user_input == "2005":
    print("They are a Rooster!")

elif friend_user_input == "2006":
    print("They're a Dog!")

elif friend_user_input == "2007":
    print("They are a Pig! (No offense)")

elif friend_user_input == "2008":
    print("They're a Mouse!")

elif friend_user_input == "2009":
    print("They are an Ox!")

elif friend_user_input == "2010":
    print("They're a Tiger!")

elif friend_user_input == "2011":
    print("They are a Rabbit!")

######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
