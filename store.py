'''docstring for the file overall
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103

productArray = []

def addProduct(self, price, name, weight, brand, cost, status="for sale"):
    '''This function will remove the product from the system
    '''
    self.price = price
    self.name = name
    self.weight = weight
    self.brand = brand
    self.cost = cost
    self.status = status
    productArray.append([self.name, self.brand, self.price,
                         self.weight, self.cost, self.price])
    # in real world, I would prompt the user for input to get this information.
    # in this case, I am passing it in.

def removeProduct(self):
    '''This function will remove the product from the system
    '''
    pass
    #prompt the person to enter the product name, remove it.

def seeInventory(self):
    '''This function will print a list of all the inventory at a given store.
        Initially I have this working for one store, Bellevue only.
    '''
    print productArray

class Stores(object):
    '''This is the stores class, which holds information about the stores.
    '''
    def __init__(self, name, address, city, state, zipcode, ownername="Troy Center"):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.ownername = ownername
    
    def storeInfo(self):
        '''This function displays all the Store information.
        '''
        print "====================================="
        print "== Store info for ", self.name, " =="
        print "====================================="
        print "Store Name: ", self.name
        print "Address: ", self.address
        print "City, State, Zip:", self.city, self.state, self.zipcode
        print "Owners Name: ", self.ownername
        return self

class Products(object):
    '''This is the product class which holds information about the products.
    '''
    def __init__(self, price, name, weight, brand, cost, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        productArray.append([self.name, self.brand, self.price,
                             self.weight, self.cost, self.price])

    def addProduct(self, price, name, weight, brand, cost, status="for sale"):
        '''This function will remove the product from the system
        '''
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
        productArray.append([self.name, self.brand, self.price,
                            self.weight, self.cost, self.price])
        # in real world, I would prompt the user for input to get this information.
        # in this case, I am passing it in.

def removeProduct(self):
    '''This function will remove the product from the system
    '''
    pass
    #prompt the person to enter the product name, remove it.

def seeInventory(self):
    '''This function will print a list of all the inventory at a given store.
        Initially I have this working for one store, Bellevue only.
    '''
    print productArray

    def productInfo(self):
        '''This fucntion shows all the product details.
        '''
        print "====================================="
        print "== Price info for ", self.name, " =="
        print "====================================="
        print "Price: $", format(self.price, '.2f')
        print "Product: ", self.name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Cost: $", format(self.cost, '.2f')
        print "Status: ", self.status
        return self


Bellevue = Stores("Bellevue", "10260 NE 25th St", "Bellevue", "WA", "98004")
Bellevue.storeInfo()
Everett = Stores("Everett", "805 80th Ave SW", "Everett", "WA", "98109")
Everett.storeInfo()
Kenmore = Stores("Kenmore", "7500 Kenmore Ave", "Kenmore", "WA", "98115")
Kenmore.storeInfo()
Seattle = Stores("Seattle", "901 Fifth Ave", "Seattle", "WA", "98164")
Seattle.storeInfo()

laptop = Products(2199.99, "EliteBook", "6lbs", "HP", 1400.00)
laptop.productInfo()
laptop2 = Products(3199.99, "GameBook G4", "10lbs", "HP", 2400.00)
laptop2.productInfo()
laptop3 = Products(499.99, "StudentModel", "5lbs", "Dell", 310.00)
laptop3.productInfo()
dockingstation = Products(199.99, "EliteDock", "2lbs", "HP", 149.00)
dockingstation.productInfo()
speaker = Products(199.99, "ProAudio5.1", "8lbs", "Klipsch", 159.00)
speaker.productInfo()
monitor = Products(299.99, "HR24", "4lbs", "Dell", 210.00)
monitor.productInfo()
cpu = Products(199.99, "i7-4400", "0lbs", "Intel", 180.00)
cpu.productInfo()
memory = Products(39.99, "16GB DDR3", "0lbs", "Crucial", 19.00)
memory.productInfo()
powersupply = Products(49.99, "Power420", "3lbs", "Corsair", 21.00)
powersupply.productInfo()
vgacable = Products(19.99, "VGA Cable", "1lbs", "C2G", 10.00)
vgacable.productInfo()
printercable = Products(19.99, "USB Printer Cable", "1lbs", "C2G", 10.00)
printercable.productInfo()
powercable = Products(19.99, "Power Cable", "1lbs", "C2G", 10.00)
powercable.productInfo()
smhdd = Products(199.99, "HDD120GB5400", "2lbs", "Seagate", 140.00)
smhdd.productInfo()
lghdd = Products(299.99, "HDD240GB7200", "2lbs", "Seagate", 190.00)
lghdd.productInfo()

addProduct(19.99, "Screen Cleaner", "1lb", "Gelco", 12.00, "for sale")
