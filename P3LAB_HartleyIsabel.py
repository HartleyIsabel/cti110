'''
Isabel Hartley
20 Oct 2024
P3LAB
Writing a python program for banking
'''

def calculate_coins(amount):
    cents = int(round(amount * 100))

    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    results = []
    
    if dollars > 0:
        results.append(f"{dollars} dollar" + ("s" if dollars > 1 else ""))
    if quarters > 0:
        results.append(f"{quarters} quarter" + ("s" if quarters > 1 else ""))
    if dimes > 0:
        results.append(f"{dimes} dime" + ("s" if dimes > 1 else ""))
    if nickels > 0:
        results.append(f"{nickels} nickel" + ("s" if nickels > 1 else ""))
    if pennies > 0:
        results.append(f"{pennies} penny" + ("ies" if pennies > 1 else ""))
    
    if not results:
        return "no change"
    
    return ', '.join(results)


try:
    user_input = float(input("Enter the amount of money as a float: $"))
    if user_input < 0:
        print("Please enter a non-negative amount.")
    else:
        result = calculate_coins(user_input)
        print(result)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
