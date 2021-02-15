class RetailItem:

    # Initialize all required arguments
    def __init__(self, itemDesc, units, price):
        self.__itemDesc = itemDesc
        self.__units = units
        self.__price = price

    # Display item description
    def getdesc(self):
        return self.__itemDesc

    # Display the units in investory
    def getunits(self):
        return self.__units

    # Display the unit price
    def getprice(self):
        return self.__price