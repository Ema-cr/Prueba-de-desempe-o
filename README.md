# Riwi Store - Inventory Management

This program allows you to manage a shopping list in an online store. Users can add products, view the product list, update prices, delete products, and calculate the total inventory value.

## Features

### 1. **Add product**

Allows the user to add a product to the store inventory by providing:

* Name of the product.
* Price of the product.
* Quantity of the product.

Validations are performed to ensure that the name is not empty or contains numbers, that the price is a positive number, and that the quantity is a positive integer.

### 2. **Check products**

Allows the user to search for a product by name. If the product is listed, the name, available quantity, and price of each unit are displayed.

### 3. **Update price**

Allows the user to update the price of an existing product in the shopping list. The product name and new price must be entered.

### 4. **Delete product**

Allows the user to remove a product from the shopping list by providing the product name.

### 5. **See the total value**

Shows the total purchase value, adding the price of all products multiplied by their respective quantity.

### 6. **See all the products**

Displays all products in inventory.

### 0. **Exit the menu**

---

## Instructions for Use

1. Clone or download this repository to your computer.

2. Open a terminal or console and navigate to the folder where the `tienda.py` file is located.

3. Once the program is run, a menu with several options will appear. The user can interact with the program by choosing options from the menu.

---

## Options Menu

```
Welcome to the Riwi Store!. What do you want to do?. : 
------------------Menu-------------------------------
1. Add products to inventory.
2. Check products in inventory.
3. Update product prices.
4. Remove products from inventory.
5. Calculate the total value of the inventory.
6. Show all the products in the inventory.
0. Quit.
```

### Options:

* **Option 1**: Add product.
* **Option 2**: Check product.
* **Option 3**: Update prices.
* **Option 4**: Delete product
* **Option 5**: See the total value.
* **Option 6**: See all the products.
* **Option 0**: Exit the menu.

---

## Usage Example


```plaintext
Welcome to the Riwi Store!. What do you want to do?. : 
------------------Menu-------------------------------
1. Add products to inventory.
2. Check products in inventory.
3. Update product prices.
4. Remove products from inventory.
5. Calculate the total value of the inventory.
6. Show all the products in the inventory.
0. Quit.

Select an option: 1
Enter the name of the desired product: Apples
Enter the price of the desired product: 2.50
Enter the quantity you want: 10
Product added successfully.

List of all products:
10 units of Apples at $2.50 each

Select one option: 5
The sum of all products is: $25.00
```
---

## Code Structure

* **`add_products()`**: Allows you to add products to the inventory with the necessary validations.
* **`check_products()`**: Allows you to search for products by name in the inventory.
* **`update_price()`**: Allows you to update the price of a product in the inventory
* **`remove_products()`**: Allows you to remove a product from inventory
* **`show_total()`**: Calculates and displays the total inventory
* **`list_of_prods()`**: Shows all the products that are in the inventory
* **`Menu()`**: User interface that allows you to choose a menu option and execute the corresponding function.

---

## Contribución

If you'd like to improve this project or add new features, feel free to create a pull request!

---
