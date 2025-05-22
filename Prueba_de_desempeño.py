inventory=[] #List to store all products
burn1={"name": "mango","price": 4000,"quantity": 5}     # Lists of producst already put in the inventory
burn2={"name": "watermelon", "price": 5000,"quantity":2}
burn3={"name": "potato", "price": 2000,"quantity":3}
burn4={"name": "avocado", "price": 3500,"quantity":2}
burn5={"name":"coconut", "price": 5000, "quantity":3}
inventory.append(burn1) #commands to put products into inventory
inventory.append(burn2)
inventory.append(burn3)
inventory.append(burn4)
inventory.append(burn5)

#Main menu function
def menu():
    while True: #Show the options in the menu
        print("""
Welcome to the Riwi Store!. What do you want to do?. : 
------------------Menu-------------------------------
1. Add products to inventory.
2. Check products in inventory.
3. Update product prices.
4. Remove products from inventory.
5. Calculate the total value of the inventory.
6. Show all the products in the inventory.
0. Quit.""")
#----------------------------------------------------------------------------------------------------------------------------------------------------------       
        option=input("Select one option from the menu: ").strip() #Read the option that the user chooses
        #Execute the corresponding option
        if option == "1":
            add_products()
#------------------------------------------------------------------------------------------------------------------------------------------------------------            
        elif option == "2":  # Search for a product by name and print the details.
            product_to_find=input("What product do you want to search?: ").strip()
            result=check_products(product_to_find, inventory)
            if result:
                print(f"Found: {result['name']} to {result['price']} with {result['quantity']} units. ") #Displays the found product and details
            else:
                print("Product not found. ") #Displays if the product is not found
 #------------------------------------------------------------------------------------------------------------------------------------------------------------                 
        elif option == "3": # Updates the price of a product.
            product_to_find=input("Enter the name of the product you want to update the price: ").strip() #Enter the product for which you want to update the price
            try:
                new_price = float(input(f"Enter the new price for '{product_to_find}': ")) #Enter the price to update the product
                if new_price < 0:    #check that it is a positive number.
                    print ("The price must be greater than zero.")
                else:
                    update_price(product_to_find, new_price) # Call the function to update the price.
            except ValueError:
                    print("The price must be a valid number.") # If the entered price is not valid, an error is displayed.
 #------------------------------------------------------------------------------------------------------------------------------------------------------------                     
        elif option == "4": # Remove a product from the list.
            name=input("Enter the name of the product you want to delete: ").strip()
            remove_products(name) # Call the function to delete the desired product
 #------------------------------------------------------------------------------------------------------------------------------------------------------------             
        elif option == "5": # Displays the total purchase.
            total_price = show_total() #the lambda function is called for show the total price
            print(f"The sum of all products is: $ {total_price:.2f}")
 #------------------------------------------------------------------------------------------------------------------------------------------------------------        
        elif option == "6": # Call a function to show all the products in the inventary
            list_of_prods() 
            
        elif option == "0": # Option to exit the menu
            print("Thank you for using the Riwi Store System!")
            break # Break to exit the menu function
        else:
            print("Invalid option, please choose an option from the menu.") #Error if a function other than the menu is entered

#-------------------------------------------------------------------------------------------------------------------------------------------------------       

def add_products(): #Function to add products in the inventory
    while True:     #Loop until the user enters a correct name
        product_name=input("Enter the name of the product you want: ").strip()
        if product_name== "":   #If the user enters an empty name, a message is printed.
            print("The name of the product cannot be empty. Please try again.")
        else:        #break the loop when the user enters a correct name
            break 
#----------------------------------------------------------------------------------------------------------------------------------------------------------  
    while True:     #Loop until the user enters a valid price
        try:
            product_price=float(input("Enter the price of the product you want: "))
            if product_price > 0:  #check that it is a positive number.
                break
            else:
                print("Enter a valid price. ") #If it is not valid, an error is displayed.
        except ValueError:
            print("Enter a valid numerical value.") #If the user enter something other than a number, it displays another error.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    while True:
        try: #Request the quantity of the product and verify that it is a positive
            product_quantity=int(input("Enter the quantity of products you want: "))
            if product_quantity > 0:
                break    # If the amount is valid, we exit the loop.
            else:
                print("Enter a valid amount. ")
        except ValueError:
            print("Enter a valid whole number. ") # If an error occurs, indicate that it must be an integer.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Create a dictionary with the product data and add it to the inventory.
    product_list={
        "name":product_name, 
        "price":product_price,
        "quantity":product_quantity
}
   
    inventory.append(product_list)   # Add the product to the inventory.
    print("Product added successfully. ")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to search for a product by name in the inventory.
def check_products(product_to_find, inventory):
    for product in inventory:
        # Compare the product names (in lowercase to avoid caps errors).
        if product["name"].lower() == product_to_find.lower():
            return product
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to update the price of a product in the inventory.
def update_price(product_to_find, new_price):
        for product in inventory:  # Compare the product names in the inventory (in lowercase to avoid caps errors).
            if product["name"].lower() == product_to_find.lower():
                product["price"] = new_price
                print("Price updated correctly.") #If the product is found and exchanged for a valid price
                return
        else:
            print("That product dont exist in the inventory")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to remove a product from the list.
def remove_products(name):
    for i, product in enumerate(inventory):  #Scans the list to find the product the user wants to delete
        if product["name"].lower() == name.lower():
            inventory.pop(i) # Remove the product from the list.
            print("The product has been successfully removed. ")
            return  # If the product is found, it deletes it and exits the function.
    else:
        print("The product has not been found. ") # If not found, display a message.
 #-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function to calculate and display the total purchase (price * quantity).
def show_total():
    # Adds the total of the products (price * quantity) and returns it.
    return sum(map(lambda product: product.get("price", 0) * product.get("quantity", 1), inventory))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function to display all products in the inventory
def list_of_prods():
    print("List of all products: ")
    for product in inventory: #Displays the quantity, name, and price of each of the products in the inventory
        print(f"{product['quantity']} units of '{product['name']}' at this price '{product['price']:.2f}' each one ") 

menu()
