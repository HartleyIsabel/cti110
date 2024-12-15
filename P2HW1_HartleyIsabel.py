'''
Isabel Hartley
13 Oct 2024
P2HW1
showing results of a trip
'''


budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_expense = float(input("How much do you think you will spend on gas? "))
accommodation_expense = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_expense = float(input("Last, how much do you need for food? "))


total_expenses = gas_expense + accommodation_expense + food_expense
remaining_balance = budget - total_expenses


print("\n--- ----Travel Expenses--- ")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas_expense:.2f}")
print(f"Accommodation: ${accommodation_expense:.2f}")
print(f"Food: ${food_expense:.2f}")
print("--- ----")
print(f"Remaining Balance: ${remaining_balance:.2f}")
