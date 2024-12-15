'''
Isabel Hartley
29 Sept 2024
P1HW2
Creating aprgram that does some basic math on numbers that are entered
'''
budget=int(input("Enter your budget:"))
destination=input("Enter your travel destination;")
gas=int(input("Enter the amount you will spend on gas:"))
accomodation=int(input("Enter the amount you will spend on accommodation:"))
food=int(input("Enter the amount you will spend on food:"))
expenses=gas+accommodation+food
remaining_budget= budget - expenses
print("Your remaining budget for trip to", destination, "is:", remaining_budget)
