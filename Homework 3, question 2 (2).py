#===========================================================
#
#  Title:       Milk Calculator
#  Course:      CPS 120
#  Homework:    <Assignment 3, problem 3>
#  Author:      <Brandon Devereux>
#  Date:        <6 Oct 2020>
#  Description:
#       Calculates the cost of milk depending on type and amount.
#        
#
#===========================================================

# Show application header
print ("\n" * 40)  # This is needed to clear the screen
print ("Welcome to the Milk Lovers Calculator!")
print ("--------------------------\n")

# <Provides user input for calculations.>
Milk_type = str(input("Input Milk Type (w=whole; t=2percent; s=skim:"))
Gallons = int(input("Input gallon amount:"))

#formulas for milk
W = 4
w = 4
T = 3.5
t = 3.5
S = 3
s = 3
Total = (W or w) * Gallons
Total1 = (T or t) * Gallons
Total2 = (S or s) * Gallons


#This places a spaced line between input and output
print ("")

# If/else statements to make conversion work

if Milk_type == "W or w":
    print ("Milk type purchased: Whole"),
    print ("Gallons purchased:   {0:10.2f}".format(Gallons)),
    print ("Cost per gallon: ${0:13.2f}".format(W)),
    print ("Total: ${0:23.2f}".format(Total))
elif Milk_type == "T or t":
    print ("Milk type purchased: 2percent"),
    print ("Gallons purchased:   {0:10.2f}".format(Gallons)),
    print ("Cost per gallon: ${0:13.2f}".format(T)),
    print ("Total: ${0:23.2f}".format(Total1))
elif Milk_type == "S or s":
    print ("Milk type purchased: Skim"),
    print ("Gallons purchased:   {0:10.2f}".format(Gallons)),
    print ("Cost per gallon: ${0:13.2f}".format(S)),
    print ("Total: ${0:23.2f}".format(Total2))


# Show application close
print ("\nEnd of my Application")
