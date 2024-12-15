# Isabel Hartley
#17 Nov 2024
#P5LAB
#Creating a program to simulate a custormer self checkout machine


import random


def disperse_change(change):
    
    coins = [1.00, 0.25, 0.10, 0.05, 0.01]
    
    coin_names = ["dollars", "quarters", "dimes", "nickels", "pennies"]
    
   
    for i in range(len(coins)):
        coin_count = int(change // coins[i])  
        change -= coin_count * coins[i]          
        if coin_count > 0:  
            print(f"{coin_count} {coin_names[i]}")

def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total amount owed: ${owed:.2f}")
    
    paid = float(input("Enter the amount of money you are paying: $"))
    
    change_owed = paid - owed
    
    if change_owed < 0:
        print("Insufficient funds. Please pay more.")
    else:
        print(f"Change owed: ${change_owed:.2f}")
        disperse_change(round(change_owed, 2))  

if __name__ == "__main__":
    main()
