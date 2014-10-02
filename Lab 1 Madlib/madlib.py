__author__ = 'jacobritenour'

#initial questions
response = raw_input("Please enter your name: ")
response1 = raw_input("Please enter your age: ")
response2 = raw_input("Please enter a number between 1-15: ")
response3 = raw_input("Please enter a number between 1-5: ")
response4 = raw_input("Please enter your favorite color: ")
response5 = raw_input("Please enter your favorite outdoor activity: ")
response6 = raw_input("Please enter your favorite indoor activity: ")
response7 = raw_input("Are you married? Yes or No: ")
response8 = raw_input("Do you have children? Yes or No: ")
response9 = raw_input("If you could be an animal what would it be: ")
response10 = raw_input("If you could have a Super Power what would it be: ")


print "It is nice to finally meet you " + response + " I am Dr. Jogue"

if response1 < 30:
    print "You may just now be feeling the effects of the serum you were given as a child."
else:
    print "I am curious to run some tests to see why you have not been affected by the serum you were given as a child."

print "We gave you " + response2 + "ml of the serum"

print "The type of serum would have caused your to become a " + response4 + " colored " + response9

print "We observed you doing the " + response5 + " activity one day last week at the beach."


if response7 = "yes":
    print "We here at the lab are happy to see also that during your " + response6 + " activities "
else:
    print "We see that with all of your " + response6 + " activities have yet to find a suitable and sustainable mate. Humm we must correct that."