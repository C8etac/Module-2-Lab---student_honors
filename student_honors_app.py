"""
Author: Catelynn Barfell
Date written: 10/31/24
Assignment: Module 2 Lab - Case Study: if...else and while
File Name: student_honors_app.py
Description: Student_honors_app.py accepts a student's last name, first name, and GPA, 
and checks if the student qualifies for the Dean's List or the Honor Roll based on 
their GPA. The program will continue to process student records until 'ZZZ' is entered 
as the last name. """

# Begin processing student records
while True:
    # Prompt for students last name; exit if 'ZZZ' is entered
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()
    if last_name.upper() == "ZZZ":
        break  # Exit the loop if the sentinel value is entered
    
    # Prompt for students first name
    first_name = input("Enter student's first name: ").strip()
    
    # Prompt for students GPA, (float)
    try:
        gpa = float(input("Enter student's GPA: ").strip())
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue  # Prompt user again if the GPA is invalid
    
    # Check if the student qualifies for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    # Check if the student qualifies for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll.")

print("Student processing has ended.")




