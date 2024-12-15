#Isabel Harltey
#24 Nov 2024
#P5HW
#A program that gives simple math quizzes

import random

def addition_quiz():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    print(f"What is {num1} + {num2}?")
    
    correct_answer = num1 + num2
    guess_count = 0
    user_answer = None
    
    while user_answer != correct_answer:
        try:
            user_answer = int(input("Your answer: "))
            guess_count += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses.")
            elif user_answer < correct_answer:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def subtraction_quiz():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    
    if num1 < num2:
        num1, num2 = num2, num1
    
    print(f"What is {num1} - {num2}?")
    
    correct_answer = num1 - num2
    guess_count = 0
    user_answer = None
    
    while user_answer != correct_answer:
        try:
            user_answer = int(input("Your answer: "))
            guess_count += 1
            
            if user_answer == correct_answer:
                print(f"Congratulations! You got it right in {guess_count} guesses.")
            elif user_answer < correct_answer:
                print("Your guess is too low. Try again.")
            else:
                print("Your guess is too high. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    while True:
        print("\nMath Quiz Menu")
        print("1. Addition Quiz")
        print("2. Subtraction Quiz")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            
            if choice == 1:
                addition_quiz()
            elif choice == 2:
                subtraction_quiz()
            elif choice == 3:
                print("Thank you for playing! Goodbye.")
                break  
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

display_menu()
