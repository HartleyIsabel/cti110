'''
Isabel Hartley
03 Nov 2024
P4LAB2
Writing a program that asks the user to enter an integer.
'''
def multiplication_table(n):
    """Display the multiplication table for a given integer n."""
    print(f"\nMultiplication Table for {n}:")
    for i in range(1, 13): 
        print(f"{n} x {i} = {n * i}")

def main():
    run_again = True  

    while run_again:
        user_input = input("Enter an integer: ")
        
        try:
            number = int(user_input)
            if number < 0:
                print("Cannot accept negative values. Please try again.")
            else:
                multiplication_table(number)  

        except ValueError:
            print("Invalid input. Please enter an integer.")
        
        repeat = input("Do you want to run the program again? (yes/no): ").strip().lower()
        if repeat != 'yes':
            run_again = False  

    print("Goodbye!")  

if __name__ == "__main__":
    main()
