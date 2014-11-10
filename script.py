from bike_classes import BikeShop
from bike_classes import Bicycle
from bike_classes import Customer

# Create 6 bikes

schwinn = Bicycle("Schwinn", cost=100, weight=15)
atrek = Bicycle("Atrek", cost=200, weight=20)
roadmaster = Bicycle("Mongoose", cost=400, weight=5)
gt = Bicycle("GT", cost=400, weight=10)
phillips = Bicycle("Phillips", cost=350, weight=15)
cube = Bicycle("Cube", cost=600, weight=10)

# Create 3 customers

jane = Customer("Jane", fund=600)
george = Customer("George", fund=300)
billy = Customer("Billy", fund=200)

# Create a customer list for ease of iteration

customers = [jane, george, billy]


# Create a bike Shop

mnmshop = BikeShop("MnM's Bike Shop")

# Add bikes to the inventory

mnmshop.add_bike(schwinn.model, schwinn.cost, number_of_bikes=10)
mnmshop.add_bike(atrek.model, atrek.cost, number_of_bikes=10)
mnmshop.add_bike(roadmaster.model, roadmaster.cost, number_of_bikes=1)
mnmshop.add_bike(gt.model, gt.cost, number_of_bikes=5)
mnmshop.add_bike(phillips.model, phillips.cost, number_of_bikes=5)
mnmshop.add_bike(cube.model, cube.cost, number_of_bikes=6)

# Print the bike inventory before anyone purchases anything

for bicycle in mnmshop.inventory:
    print "We have " + str(mnmshop.inventory[bicycle]) \
          + " " + bicycle + " bicycles in stock."

# Make a list for each customer of bikes they can afford.

def affordable_list(name):
    bike_list = []
    for cost in mnmshop.bicycles:
        if mnmshop.bicycles[cost] < name.fund:
            bike_list.append(cost)
    return bike_list

jane_list = affordable_list(jane)
george_list = affordable_list(george)
billy_list = affordable_list(billy)

print "Jane can afford to buy the following bikes: " 
print jane_list
for item in jane_list:
    print item, 

print "George can afford to buy the following bikes: " 
for item in george_list:
    print item

print "Billy can afford to buy the following bikes: " 
for item in billy_list:
    print item

# Print the name of the customers and the bikes each one can afford.



