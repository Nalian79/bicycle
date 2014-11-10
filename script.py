import random
from bike_classes import BikeShop
from bike_classes import Bicycle
from bike_classes import Customer

# Create 6 bikes
print "Creating 6 bicycles... \n"

schwinn = Bicycle("Schwinn", cost=100, weight=15)
atrek = Bicycle("Atrek", cost=200, weight=20)
roadmaster = Bicycle("Mongoose", cost=400, weight=5)
gt = Bicycle("GT", cost=400, weight=10)
phillips = Bicycle("Phillips", cost=350, weight=15)
cube = Bicycle("Cube", cost=600, weight=10)

# Create 3 customers
print "Creating customers to purchase inventory... \n"

jane = Customer("Jane", fund=800)
george = Customer("George", fund=500)
billy = Customer("Billy", fund=300)

# Create a bike Shop
print "Creating the Bike Shop... \n"
mnmshop = BikeShop("MnM's Bike Shop")
print mnmshop.name + " is now live! \n"
# Add bikes to the inventory

print "Adding bicycles to the inventory of " + mnmshop.name + ": \n"

mnmshop.add_bike(schwinn.model, schwinn.cost, number_of_bikes=10)
mnmshop.add_bike(atrek.model, atrek.cost, number_of_bikes=7)
mnmshop.add_bike(roadmaster.model, roadmaster.cost, number_of_bikes=2)
mnmshop.add_bike(gt.model, gt.cost, number_of_bikes=5)
mnmshop.add_bike(phillips.model, phillips.cost, number_of_bikes=3)
mnmshop.add_bike(cube.model, cube.cost, number_of_bikes=6)

# Print the bike inventory before anyone purchases anything

print "\n"
print "We are proud to carry a wide range of bikes in stock! \n"

def bike_inventory():
    for bicycle in mnmshop.inventory:
        print "We have " + str(mnmshop.inventory[bicycle]) \
            + " " + bicycle + " bicycles in stock."

bike_inventory()
print " \n"


# Make a list for each customer, containing the bikes they can afford.

def affordable_list(name):
    bike_list = []
    for cost in mnmshop.bicycles:
        if mnmshop.price_bike(cost) < name.fund: 
            bike_list.append(cost)
    return bike_list

jane_list = affordable_list(jane)
george_list = affordable_list(george)
billy_list = affordable_list(billy)

# Print the list of bikes each customer can afford

print "Jane has " + str(jane.fund) + " dollars to spend." 
print "Jane can afford to buy the following bikes: " 
for item in jane_list:
    print item, 

print "\n"
print "George can afford to buy the following bikes: " 
for item in george_list:
    print item,

print "\n"
print "Billy can afford to buy the following bikes: " 
for item in billy_list:
    print item,

# Make the customers purchase a bike, print the bike name, cost, and leftover customer funds.

jane_choice = random.choice(jane_list)
george_choice = random.choice(george_list)
billy_choice = random.choice(billy_list)

print "\n"
print "Jane chooses to buy the " + jane_choice + " bicycle. \n"
jane.buy_bike(bike_name=jane_choice, cost=mnmshop.price_bike(jane_choice))
mnmshop.sell_bike(bicycle=jane_choice)
print "Jane has " + str(jane.fund) + " dollars left. \n"

print "\n"
print "George chooses to buy the " + george_choice + " bicycle. \n" 
george.buy_bike(bike_name=george_choice, cost=mnmshop.price_bike(george_choice))
mnmshop.sell_bike(bicycle=george_choice)
print "George has " + str(george.fund) + " dollars left. \n"

print "\n"
print "Billy chooses to buy the " + billy_choice + " bicycle. \n"
billy.buy_bike(bike_name=billy_choice, cost=mnmshop.price_bike(billy_choice))
mnmshop.sell_bike(bicycle=billy_choice)
print "Billy has " + str(billy.fund) + " dollars left. \n"


# Print out the inventory post customer purchasing

print "After purchases, we have the following bikes left: "
bike_inventory()

print "\n"
print "The shop has made " + str(mnmshop.profit) + " dollars in profit."
