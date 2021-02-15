# Import the Retail Item Class
import RetailItemClass as rc

# Define the main function
def main():

    # Create an empty list to hold the retail item
    retail_list = list()

    # Request number of records to store from users
    num_items = int(input("Enter number of retail records to store: "))
    print()

    for i in range(1, num_items + 1):
        itemDesc = input("Enter Item Description #" + str(i) + ": ")
        units = int(input("Enter Unit #" + str(i) + ": "))
        price = float(input("Enter Price #" + str(i) + ": "))
        print("-----")

        # Create an object of the RetailItem Class
        retail = rc.RetailItem(itemDesc, units, price)

        # Append the object to the empty list
        retail_list.append(retail)

    # Display output
    print()
    print("\t\t\t\tRetail Items")
    print(
        "--------------------------------------------------------------------------------"
    )
    print("", "\t\tDescription", "\t\tUnits in Inventory", "\t\tPrice")
    print(
        "--------------------------------------------------------------------------------"
    )

    for i in range(num_items):

        # Space between Description and Units Columns
        row_space = (30 - len(retail_list[i].getdesc())) * " "

        # Display using the methods in the class and accompanying index numbers from the list
        print(
            "Item #",
            i + 1,
            "\t\t",
            retail_list[i].getdesc(),
            row_space,
            retail_list[i].getunits(),
            "\t\t\t",
            "$",
            format(retail_list[i].getprice(), ",.2f"),
            sep="",
        )


main()