import os
class ShoppingCart():
  def __init__(self, item_name, item_price, item_description):
    self.item_name = item_name
    self.item_price = item_price
    self.item_description = item_description
  def item_details(self):
    return print(self.item_name,self.item_price,self.item_description)


storage = []
choice = 0
while choice != 'E':
  print("Main menu")
  print("C: Add a new item")
  print("R: Read (Display) your shopping cart")
  print("D: Delete an item")
  print("E: Exit the program")
  choice = str(input("Your choice : ")).upper()

  if choice == 'C':
    os.system('clear')
    name = input("Input Name of the item: ")
    price = input("Input Price of the item: ")
    description = input("Input Description of the item: ")
    
    my_items = ShoppingCart(name, price, description)
    
    storage.append(my_items)
    print("Item successfully inputted!\n")
    
  elif choice == 'D':
    os.system('clear')

    print("Shopping Cart")
    for x in range(len(storage)):
      storage[x].item_details()
      
    if len(storage) == 0:
      print("Shopping cart is empty!")
    else:
      index = input("Index of data you want to delete from your shopping cart:")
      if index.isnumeric() == False:
        print("Index is invalid (not a number)")    
      else: 
        index = int(index)
        if index+1 > len(storage):
          print("Index out of range!")
        else:
          del storage[index]
          print("Data successfully deleted!\n")

  elif choice == 'R':
    os.system('clear')
    if len(storage) == 0:
      print("Your shopping cart is empty!\n")
    else:
      print("Shopping Cart")
      for x in range(len(storage)):
        storage[x].item_details()

  elif choice == 'E':
    print("Program Exited!")
    break
  else:
        print("Only input C,R,D and E")