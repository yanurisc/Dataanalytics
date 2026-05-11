#Lab 1

#Total due is determined by: food cost + tax + tip


#Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

#calculate the unknown
total_due = food_cost + tax + tip 

#Display the results 
print("the total due is " + str(total_due))

# str() converts a number into a string so it can be combined with other text using the + sign
# Without str(), Python would give an error because you cannot join a number and a string together 


print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))