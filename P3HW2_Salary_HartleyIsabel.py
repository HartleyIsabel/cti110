'''
Isabel Hartley
27 Oct 2024
P3WH1
Creating a program
'''
"""
Pseudocode:
1. Start
2. Define a function 'get_employee_info()' to:
   a. Prompt user for employee's name and store it in 'employee_name'
   b. Prompt user for hours worked and validate input
   c. Prompt user for pay rate and validate input
   d. Return employee_name, hours_worked, pay_rate
3. Define a function 'calculate_pay(hours_worked, pay_rate)' to:
   a. If hours_worked > 40:
       i. Set overtime_hours = hours_worked - 40
       ii. Set regular_hours = 40
       iii. Calculate overtime_pay = overtime_hours * pay_rate * 1.5
     Else:
       i. Set regular_hours = hours_worked
       ii. Set overtime_hours = 0
       iii. Set overtime_pay = 0
   b. Calculate regular_pay = regular_hours * pay_rate
   c. Calculate gross_pay = regular_pay + overtime_pay
   d. Return regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay
4. Define a function 'display_pay_info(employee_name, pay_rate, hours_worked, regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay)' to:
   a. Print all relevant pay information
5. In the main section of the program:
   a. Call 'get_employee_info()' to retrieve employee details
   b. Call 'calculate_pay(hours_worked, pay_rate)' and store returned values
   c. Call 'display_pay_info()' to show results
6. End
"""

def get_employee_info():
    employee_name = input("Enter the employee's name: ")

    while True:
        try:
            hours_worked = float(input("Enter the number of hours worked this week: "))
            if hours_worked < 0:
                print("Hours worked cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            pay_rate = float(input("Enter the employee's pay rate: "))
            if pay_rate < 0:
                print("Pay rate cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return employee_name, hours_worked, pay_rate

def calculate_pay(hours_worked, pay_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
        overtime_pay = overtime_hours * pay_rate * 1.5
    else:
        regular_hours = hours_worked
        overtime_hours = 0
        overtime_pay = 0

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    return regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay

def display_pay_info(employee_name, pay_rate, hours_worked, regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay):
    print(f"\nEmployee Name: {employee_name}")
    print(f"Pay Rate: ${pay_rate:.2f}")
    print(f"Hours Worked: {hours_worked:.2f}")
    print(f"Regular Hours: {regular_hours:.2f}")
    print(f"Overtime Hours: {overtime_hours:.2f}")
    print(f"Overtime Pay: ${overtime_pay:.2f}")
    print(f"Regular Pay: ${regular_pay:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")

def main():
    employee_name, hours_worked, pay_rate = get_employee_info()
    regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay = calculate_pay(hours_worked, pay_rate)
    display_pay_info(employee_name, pay_rate, hours_worked, regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay)

main()
