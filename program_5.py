# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

# By Nathan Nelsen
# Written 2/5/26
# Hot Dog

hot_dog_price = 3.50
chili_dog_price = 4.50
cheese_price = 0.50
peppers_price = 0.75
grilled_onions_price = 1.00
tax_rate = 0.07

print("Hot Dogs:")
print("1 - Hot Dog ($3.50)")
print("2 - Chili Dog ($4.50)")
choice = input("Which hot dog would you like? (1 ot 2): ")

cost = 0

if choice == "1":
    cost = hot_dog_price
elif choice == "2":
    cost = chili_dog_price

choice = input("Would you like cheese for $0.50? (Y/N): ")
if choice == "Y":
    cost +=cheese_price

choice = input("Would you like peppers for $0.75? (Y/N): ")
if choice == "Y":
    cost +=peppers_price

choice = input("Would you like grilled onions for $1.00? (Y/N): ")
if choice == "Y":
    cost +=grilled_onions_price

tax = cost*tax_rate
total = cost + tax

print("Total before taxes: $", cost)
print("Tax: $", round(tax,2))
print("Total: $", total)
