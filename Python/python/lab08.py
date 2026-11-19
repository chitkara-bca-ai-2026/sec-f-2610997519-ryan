# Lab 08: School Result Processing Flowchart
# 5 Subjects Loop

# Start
print("===== STUDENT RESULT PROCESSING =====")

# Input student details
name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Initialize
total = 0
i = 1
has_failed = False

# Loop for 5 subjects
while i <= 5:

    mark = int(input(f"Enter mark for Subject {i} (0-100): "))

    # Validate mark
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100")
        continue

    # Check if subject is failed
    if mark < 40:
        has_failed = True

    # Add mark to total
    total = total + mark

    # Move to next subject
    i = i + 1


# Calculate percentage
percentage = (total / 500) * 100


# Display result
print("\n========================================")
print("          STUDENT REPORT CARD")
print("========================================")
print(f"Name       : {name}")
print(f"Roll Number: {roll_number}")
print("Subjects   : 5")
print(f"Total      : {total} / 500")
print(f"Percentage : {percentage:.2f}%")


# Check result and grade
if has_failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"

else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"

    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"

    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"

    elif percentage >= 60:
        grade = "C"
        remarks = "Good"

    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"

    else:
        grade = "E"
        remarks = "Marginal Pass"


# Print final result
print(f"Result     : {result}")
print(f"Grade      : {grade}")
print(f"Remarks    : {remarks}")
print("========================================")
