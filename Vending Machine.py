class VendingMachine:
    
    def __init__(self):
        print("""
┌───────────────────────────────────────────────────────────────── •✧✧• ─────────────────────────────────────────────────────────────────┐
 - _    _ # _______ # ______  # _____   # _____ # ______  #  ______ #  # ______  #        #  ______ # _     _ # _____ # ______  # _______ #
| |  | |#(_______)#|  ___ \ #(____ \  #(_____)#|  ___ \ # / _____)#  #|  ___ \ #   /\   # / _____)#| |   | |#(_____)#|  ___ \ #(_______)#
| |  | |# _____   #| |   | |# _   \ \ #   _   #| |   | |#| /  ___ #  #| | _ | |#  /  \  #| /      #| |__ | |#   _   #| |   | |# _____   #
 \ \/ / #|  ___)  #| |   | |#| |   | |#  | |  #| |   | |#| | (___)#  #| || || |# / /\ \ #| |      #|  __)| |#  | |  #| |   | |#|  ___)  #
  \  /  #| |_____ #| |   | |#| |__/ / # _| |_ #| |   | |#| \____/|#  #| || || |#| |__| |#| \_____ #| |   | |# _| |_ #| |   | |#| |_____ #
   \/   #|_______)#|_|   |_|#|_____/  #(_____)#|_|   |_|# \_____/ #  #|_||_||_|#|______|# \______)#|_|   |_|#(_____)#|_|   |_|#|_______)#
        ##         ##         ##         ##       ##         ##         ##  ##         ##        ##         ##         ##       ##         ##
└───────────────────────────────────────────────────────────────── •✧✧• ─────────────────────────────────────────────────────────────────┘""")
        self.items = {
            'Drinks': [
                {'code': 'A1', 'name': 'Cola', 'price': 1.50, 'quantity': 5},
                {'code': 'A2', 'name': 'Water', 'price': 1.00, 'quantity': 10},
                {'code': 'A3', 'name': 'Orange Juice', 'price': 1.75, 'quantity': 8},
                {'code': 'A4', 'name': 'Iced Tea', 'price': 1.25, 'quantity': 7},
                {'code': 'A5', 'name': 'Coffee', 'price': 1.80, 'quantity': 6}
            ],
            'Snacks': [
                {'code': 'B1', 'name': 'Chips', 'price': 1.00, 'quantity': 8},
                {'code': 'B2', 'name': 'Chocolate', 'price': 1.20, 'quantity': 6},
                {'code': 'B3', 'name': 'Pretzels', 'price': 1.30, 'quantity': 9},
                {'code': 'B4', 'name': 'Granola Bar', 'price': 1.50, 'quantity': 5},
                {'code': 'B5', 'name': 'Mixed Nuts', 'price': 1.75, 'quantity': 7}
            ]
        }
        self.user_balance = 0.0

    def display_menu(self):
        print("Welcome to the Vending Machine!\n")
        for category, category_items in self.items.items():
            print(f"{category}:\n")
            print("Code | Item           | Price | Quantity")
            print("----------------------------------------")
            for item in category_items:
                print(f"{item['code']}    | {item['name']:<15} | ${item['price']:.2f} | {item['quantity']}")
            print("\n")

    def accept_money(self):
        try:
            amount = float(input("Please insert money: $"))
            if amount < 0:
                print("Invalid amount. Please insert a positive amount.")
                return 0
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            return 0

    def select_item(self):
        item_code = input("Enter the code of the item you want to purchase: ")
        for category_items in self.items.values():
            for item in category_items:
                if item['code'] == item_code and item['quantity'] > 0:
                    return item
        print("Invalid item code or item out of stock. Please try again.")
        return None

    def dispense_item(self, item):
        print(f"\nDispensing {item['name']}...")
        item['quantity'] -= 1
        return item

    def print_receipt(self, item):
        print("\nReceipt:")
        print("+----------------------+")
        print("| Item: {0:<17} |".format(item['name']))
        print("| Price: ${0:<13.2f} |".format(item['price']))
        print("| Amount Paid: ${0:<9.2f} |".format(self.user_balance))
        print("| Change: ${0:<12.2f} |".format(self.user_balance - item['price']))
        print("+----------------------+")
        print("Thank you for your purchase!\n")

    def return_change(self, change):
        if change > 0:
            print(f"Returning change: ${change:.2f}")
        else:
            print("No change to return.")

    def run_vending_machine(self):
        while True:
            self.display_menu()
            self.user_balance += self.accept_money()

            item = self.select_item()
            if item:
                if self.user_balance >= item['price']:
                    self.dispense_item(item)
                    change = self.user_balance - item['price']
                    self.return_change(change)
                    self.user_balance = 0.0
                else:
                    print("Insufficient funds. Please insert more money or choose a cheaper item.")
            else:
                print("Transaction canceled.")
            
            continue_shopping = input("Do you want to continue shopping? (y/n): ").lower()
            if continue_shopping != 'y':
                print("Thank you for using the Vending Machine. Have a great day!")
                break


# Example usage
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_vending_machine()
