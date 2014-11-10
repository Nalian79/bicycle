class Bicycle(object):
    """Create a bicycle object for use with the BikeShop class."""
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class BikeShop(object):
    """A BikeShop class for making and running your own bicycle shop."""
    def __init__(self, name):
        self.name = name
        self.inventory = {}
        self.bicycles = {}
        self.profit = 0

    def add_bike(self, bicycle, cost, number_of_bikes=1):
        """Add a bicycle to our inventory of bikes."""
        if not bicycle in self.bicycles:
            self.bicycles[bicycle] = cost
            self.inventory[bicycle] = number_of_bikes
            print bicycle + " added to inventory of " + str(self.name) + "."
        else:
            self.inventory[bicycle] = self.inventory[bicycle] + number_of_bikes 
            print "You now have " + str(self.inventory[bicycle]) + \
                " bicycles in inventory."
        return self.bicycles, self.inventory

    def remove_bike(self, bicycle):
        """Just remove the bike from inventory."""
        if bicycle in self.inventory:
            if self.inventory[bicycle] > 1:
                self.inventory[bicycle] = self.inventory[bicycle] - 1
                print "Removed 1 " + bicycle + " from inventory."
            else:
                del self.bicycles[bicycle]
                del self.inventory[bicycle]
                print "Removed the last " + bicycle + " from inventory."
        else:
            print bicycle + " is not in inventory."
        return self.bicycles, self.inventory

    def sell_bike(self, bicycle, margin=0.2):
        """Remove bike from inventory and add margin to the profits.
        Calculate the total cost from the bicycle price + margin, print that
        out, then add the margin to the profit, and delete the bike from
        inventory.
        """
        if bicycle in self.inventory:
            pricetag = int(self.bicycles[bicycle]) + (int(self.bicycles[bicycle]) * float(margin))
            print "Selling the bicycle " + bicycle + " for " + str(pricetag)
            new_profit = pricetag - self.bicycles[bicycle]
            self.profit = self.profit + new_profit
            self.remove_bike(bicycle)
        else:
            print "I do not have any " + str(bicycle) + " in stock."
        # remove the self.bicycles once all is working
        return self.bicycles, self.inventory
        

class Customer(object):
    """Create a customer object, with a source of funds and a
    dict of bikes owned.
    """
    def __init__(self, name, fund=0.0):
        self.name = name
        self.fund = fund
        self.bicycles_owned = []
    def buy_bike(self, cost, bike_name):
        "Remove the bike cost from customer fund, add bike to customer's bicycle's owned."
        if cost > self.fund:
            print "The bike costs more than you have in funds!"
        else:
            self.fund -= cost
            self.bicycles_owned.append(bike_name)
            return self.fund, self.bicycles_owned
