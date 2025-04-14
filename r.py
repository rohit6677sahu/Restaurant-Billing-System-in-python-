# Define the menu of the restaurant
menu = {
    "pizza": 80,
    "burger": 50,
    "fries": 60,
    "coke": 30,
    "water": 40
}

# Greet the customer
print("Welcome to the restaurant!\n")
print("Would you like to have:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

# Initialize total bill
total_food = 0

# Ask for the first item
while True:
    item = input("\nWhat would you like to order (or type 'done' to finish)? ").lower()
    if item == "done":
        break
    if item in menu:
        total_food += menu[item]
        print(f"You have selected {item}.")
    else:
        print(f"Sorry, {item} is not available in the restaurant.")

# Display the total bill
print(f"\nYour total bill is Rs{total_food}. Enjoy your meal!")