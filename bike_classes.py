class Bicycle(object):
    """Create a bicycle object for use with the BikeShop class."""
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost


class BikeShop(object):
    """A BikeShop class for making and running your own bicycle shop."""
    inventory = {}
    bicycles = {}
    profit = 0
    def __init__(self, name):
        self.name = name

    def add_bike(self, bicycle, cost, number_of_bikes=1):
        """Add a bicycle to our inventory of bikes."""
        if not bicycle in self.bicycles:
            self.bicyles[bicycle] = cost
            self.inventory[bicycle] = number_of_bikes
            print bicycle + " added to inventory."
        else:
            print bicycle + " is already part of inventory."

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

    def sell_bike(self, bicycle, margin):
        """Remove bike from inventory and add margin to the profits.
        Calculate the total cost from the bicycle price + margin, print that
        out, then add the margin to the profit, and delete the bike from
        inventory.
        """
        if bicycle in self.inventory:
            pricetag = self.inventory[bicycle] + \
                (self.bicycles[bicycle] * int(margin))
            print "Selling the bicycle " + bicycle + " for " + str(pricetag)
            new_profit = pricetag - self.bicycles[bicycle]
            profit = self.profit + new_profit
            remove_bike(bicycle)
        else:
            print "I do not have " + bicycle
        

class Customer(object):
    """Create a customer object, with a source of funds and a
    dict of bikes owned.
    """
    bicycles_owned = {}
    def __init__(self, name, fund=0.0):
        self.name = name
        self.fund = fund
    def buy_bike(self, cost):
        "Remove the bike cost from customer fund, then return the fund amount."
        if cost > self.fund:
            print "The bike costs more than you have in funds!"
            break
        else:
            self.fund -= cost
            return self.fund