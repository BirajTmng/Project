#Display A Welcome Screen that says "Welcome to Inventory Management"
#Display Main Menu


import Inv

def display_main_welcome_screen():
    print("*"*50)
    print("**", " Welcome To Inventory Management System ", '**')
    print("*"*50)

def display_main_menu():
    print("1. Add Item")
    print("2. Show Item")
    print("3. View Stock")
    print("4. Show Item Code")
    print("5. View In-Date")
    print("6. Exit")
    print("*"*50)
def main():

    display_main_welcome_screen()
    
    #Main Program Loop
    while True:
        display_main_menu()

        #Take input from user 1-5
        choice = int(input("Enter a choice (1-6): "))

        if choice == 1:
            Inv.add_new_item()
        elif choice == 2:
            Inv.display_all_items()
            print("Choice 2")
        elif choice == 3:
            Inv.display_stock()
            print("Choice 3")
        elif choice == 4:
            Inv.display_item_code()
            print("Choice 4")
        elif choice == 5:
            Inv.display_in_date()
            print("Choice 5")
        elif choice == 6:
            break
        else:
            print("Invalid Choice! Try Again!")

#Run Main Function
main()