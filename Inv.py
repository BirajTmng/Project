import csv

#1. Add Item
def add_new_item():
    #Ask user to add details of new Items
    item_id = input("Enter Item ID: ")
    name = input("Enter name of Item: ")
    quantity = input("Enter Quantity of the Item: ")
    in_date= input("Enter the Purchase Date: ")

    #Create a new dictionary with input data
    newItem = [item_id, name]
    with open('./Inventory_project/Item.csv', 'a') as itemFile:
        itemWriter = csv.writer(itemFile)
        itemWriter.writerow(newItem)

    newStock = [item_id, name, quantity, in_date]
    with open('./Inventory_project/Stock.csv', 'a') as stockFile:
        stockWriter = csv.writer(stockFile)
        stockWriter.writerow(newStock)


def display_all_items():
    print("-"*80)
    print("{:<8} {:<14} {:<14} {:<15}".format(
        "Item ID", "Name", "Quantity", "In-Date"
    ))
    print("-"*80)

    with open('./Inventory_project/Stock.csv', 'r') as itemFile:
        itemFromFile = csv.reader(itemFile)
        next(itemFromFile)
        for item in itemFromFile:
            if len(item) == 4:
                print("{:<8} {:<15} {:<12} {:<14}".format(
                item[0],
                item[1],
                item[2],
                item[3]
            ))
            print("-"*80)
        else:
            print("Skipping malformed line:", item)

#3. View Stock
def display_stock():
    print("-"*80)
    print("{:<25} {:>10}".format(
        "Name", "Quantity"
    ))
    print("-"*80)

    with open('./Inventory_project/Stock.csv', 'r') as itemFile:
        itemFromFile = csv.reader(itemFile)
        next(itemFromFile)
        for item in itemFromFile:
            if len(item) == 4:
                print("{:<25} {:>10}".format(
                item[1],
                item[2]
            ))
            print("-"*80)
        else:
            print("Skipping malformed line:", item)

#4. Show Item Code
def display_item_code():
    print("-"*80)
    print("{:<25} {:>10}".format(
        "Item ID", "Name"
    ))
    print("-"*80)
    with open('./Inventory_project/Item.csv', 'r') as idFile:
        idFromFile = csv.reader(idFile)
        next(idFromFile)
        for id in idFromFile:
            if len(id) == 2:
                print("{:<25} {:>10}".format(
                id[0],
                id[1]
            ))
            print("-"*80)
        else:
            print("Skipping malformed line:", id)

#5. View In-Date
def display_in_date():
    print("-"*80)
    print("{:<25} {:>10}".format(
        "Name", "In-Date"
    ))
    print("-"*80)

    with open('./Inventory_project/Stock.csv', 'r') as itemFile:
        itemFromFile = csv.reader(itemFile)
        next(itemFromFile)
        for item in itemFromFile:
            if len(item) == 4:
                print("{:<25} {:>10}".format(
                item[1],
                item[3]
            ))
            print("-"*80)
        else:
            print("Skipping malformed line:", item)