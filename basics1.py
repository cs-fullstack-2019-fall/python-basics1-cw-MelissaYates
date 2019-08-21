# Python_Basics1_cw
#
#
# ### Problem 1:
# Create two variables. One should equal “My name is: “ and the other should equal your actual name.
# Print the two variables in one print message.
#
# ### Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.”
# If they entered more than 20 print “That’s too much extra credit”.
#
# ### Problem 3:
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
#
# ### Problem 4:
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!,
# if it’s less than 21 print “The total is [THE TOTAL]”

name = "My name is: "
nam1 = "Melissa Yates"
print(name + nam1)

user = int(input("How much extra credit did you earn"))
if(user <5):
    print("That's not enough extra credit")
elif(user>20):
    print("That's too much extra credit")

userPass = input("Please enter a password")
userPass1 = input("Please re-enter password")
if(userPass==userPass1):
    print("You are correct")
else:
    print("You are incorrect")

userCard = int(input("Please enter a card number"))
userCard1 = int(input("Please enter another number"))
total = userCard + userCard1
print(total)
if (total == 21):
    print("BLACKJACK!")
elif (total > 21):
    print("BUST!")
elif(total<21):
    print("The total is " + str(total))


