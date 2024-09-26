class VendingMachine:
   def __init__(self, soda_count, coffee_count, water_count):
       self.soda_count = soda_count
       self.coffee_count = coffee_count
       self.water_count = water_count

   def buy(self, drink_type, amount=1):
       if drink_type == 1:  # Soda
           if self.soda_count >= amount:
               self.soda_count -= amount
               print(f"Bought {amount} bottles of Soda.")
           else:
               print("Sorry, not enough Soda bottles available.")
       elif drink_type == 2:  # Coffee
           if self.coffee_count >= amount:
               self.coffee_count -= amount
               print(f"Bought {amount} bottles of Coffee.")
           else:
               print("Sorry, not enough Coffee bottles available.")
       elif drink_type == 3:  # Water
           if self.water_count >= amount:
               self.water_count -= amount
               print(f"Bought {amount} bottles of Water.")
           else:
               print("Sorry, not enough Water bottles available.")
       else:
           print("Invalid drink type.")

   def restock(self, drink_type, amount):
       if drink_type == 1:  # Soda
           self.soda_count += amount
           print(f"Restocked {amount} bottles of Soda.")
       elif drink_type == 2:  # Coffee
           self.coffee_count += amount
           print(f"Restocked {amount} bottles of Coffee.")
       elif drink_type == 3:  # Water
           self.water_count += amount
           print(f"Restocked {amount} bottles of Water.")
       else:
           print("Invalid drink type.")

   def inventory(self):
       print("Inventory")
       print(f"Soda: {self.soda_count} bottles")
       print(f"Coffee: {self.coffee_count} bottles")
       print(f"Water: {self.water_count} bottles")



def main():
   vm = VendingMachine(12, 10, 10)

   while True:
       command = input(":>").lower()

       if command == "buy":
           drink_type = int(input("Please select a drink (1 - Soda, 2 - Coffee, 3 - Water): "))
           amount = int(input("Please enter the amount: "))
           vm.buy(drink_type, amount)
       elif command == "restock":
           drink_type = int(input("Please select an option (1 - Soda, 2 - Coffee, 3 - Water): "))
                        
           amount = int(input("Please an amount: "))
           vm.restock(drink_type, amount)
       elif command == "inventory":
           vm.inventory()
       elif command == "quit" or command == "q":
           print("exiting command")
           break
       else:
           print("please try again.")


if __name__ == "__main__":
   main()