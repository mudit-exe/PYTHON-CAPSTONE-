
# ==========================================
#          CAFE MANAGEMENT SYSTEM
# ==========================================

import datetime

# Food Menu
menu = {
    1: {"name": "Coffee", "price": 80},
    2: {"name": "Tea", "price": 40},
    3: {"name": "Burger", "price": 120},
    4: {"name": "Pizza", "price": 200},
    5: {"name": "Sandwich", "price": 100},
    6: {"name": "Pasta", "price": 150},
    7: {"name": "Cold Drink", "price": 50}
}

total_sales = 0


# Function to display menu
def display_menu():
    print("\n========== CAFE MENU ==========")
    print("Item No.     Item Name       Price")

    for number, item in menu.items():
        print(f"{number}.           {item['name']:<15} Rs.{item['price']}")

    print("===============================")


# Function to place an order
def place_order():
    order = []
    total = 0

    while True:
        display_menu()

        try:
            choice = int(input("\nEnter item number (0 to finish): "))

            if choice == 0:
                break

            if choice not in menu:
                print("Invalid item number! Try again.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            item_name = menu[choice]["name"]
            price = menu[choice]["price"]

            amount = price * quantity
            total += amount

            order.append({
                "name": item_name,
                "price": price,
                "quantity": quantity,
                "amount": amount
            })

            print(item_name, "added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    if len(order) == 0:
        print("No items ordered.")
        return 0

    generate_bill(order, total)
    return total


# Function to generate bill
def generate_bill(order, total):
    print("\n========== CUSTOMER BILL ==========")
    print("Date:", datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

    print("-----------------------------------")
    print("Item       Qty      Price     Total")

    for item in order:
        print(
            f"{item['name']:<11}"
            f"{item['quantity']:<9}"
            f"{item['price']:<10}"
            f"{item['amount']}"
        )

    print("-----------------------------------")
    print("Total Amount: Rs.", total)

    print("Thank you for visiting our cafe!")
    print("===================================")

    # Save bill in file
    with open("orders.txt", "a") as file:
        file.write("\nNew Order\n")
        file.write("Date: " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + "\n")

        for item in order:
            file.write(
                f"{item['name']} x {item['quantity']} = Rs.{item['amount']}\n"
            )

        file.write(f"Total: Rs.{total}\n")
        file.write("-------------------------\n")


# Main Function
def main():
    global total_sales

    while True:
        print("\n================================")
        print("       WELCOME TO MY CAFE")
        print("================================")
        print("1. View Food Menu")
        print("2. Place an Order")
        print("3. View Total Sales")
        print("4. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                total_sales += place_order()

            elif choice == 3:
                print("\nTotal Cafe Sales: Rs.", total_sales)

            elif choice == 4:
                print("Thank you! Visit Again.")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Please enter a valid number.")


# Program Execution
if __name__ == "__main__":
    main()
