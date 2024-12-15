
#Isabel Hartley
#10 Oct 2024
#P2HW2
#Creating a program for grading


"""
Pseudocode for Grades Program (Based on Chapter 6 Concepts):

1. Begin program

2. Create a list called 'grades' to store the grades entered by the user.

3. Ask the user to enter the grade for each module:
    - Module 1: Store the grade in the 'grades' list.
    - Module 2: Store the grade in the 'grades' list.
    - Module 3: Store the grade in the 'grades' list.
    - Module 4: Store the grade in the 'grades' list.
    - Module 5: Store the grade in the 'grades' list.
    - Module 6: Store the grade in the 'grades' list.

4. Display the following information:
    - The lowest grade in the list.
    - The highest grade in the list.
    - The sum of all grades.
    - The average grade (formatted to 2 decimal places).

5. End program
"""

def main():
    
    grades = []

  
    grades.append(float(input("Enter grade for Module 1: ")))  
    grades.append(float(input("Enter grade for Module 2: ")))
    grades.append(float(input("Enter grade for Module 3: ")))  
    grades.append(float(input("Enter grade for Module 4: ")))  
    grades.append(float(input("Enter grade for Module 5: ")))  
    grades.append(float(input("Enter grade for Module 6: ")))  

    
    lowest_grade = min(grades)  
    highest_grade = max(grades)  
    total_sum = sum(grades)  
    average_grade = total_sum / len(grades)  

    
    print(f"\nLowest Grade: {lowest_grade}")
    print(f"Highest Grade: {highest_grade}")
    print(f"Sum of Grades: {total_sum}")
    print(f"Average Grade: {average_grade:.2f}")


if __name__ == "__main__":
    main()
