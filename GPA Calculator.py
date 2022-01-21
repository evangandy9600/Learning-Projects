# Evan's GPA Calculator
# Formula: (Grade point value * credits) / (total number of credits)
# How to run: 
    # Step 1) Click "F5" on keyboard to open terminal
    # Step 2) Run as python file
    # Step 3) In the bottom bar input values as you are prompted in the terminal window
    # Step 4) To weight a class, enter (W) when promted with "GPA Type: Unweighted (U) or Weighted (W) "
    # Step 5) If you prefer to calculate your unweighted GPA, enter (U) for all classes

# Dictionary

grade_dict = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}

weight_dict = {
    "AP": 1,
    "HON": 0.5,
    "REG": 0,
}

# Dictionary End

credit_values = []
point_values = []
gpa_array = []

# get grade

def get_grade():
    num_class = int(input("Number of classes: "))
    enter = 0
    while enter < num_class:
        enter += 1
        name = input("Class Name: ")
        credits = int(input(f"{name} credits: ")) # Get credits
        grade = input(f"{name} letter grade: ") # Get grade for class
        grade_point = float(grade_dict.get(grade.upper())) # Convert grade into point value
        credit_values.append(credits) # adds values to array
        point_values.append(grade_point) # adds values to array
        # Weight Calculations
        weighted = input("GPA Type: Unweighted (U) or Weighted (W) ")
        weight = ""
        if weighted.upper() == "W":
            weight = input("Chose: AP, Hon, Reg ")
            weighted_gp = credits * (weight_dict.get(weight.upper()) + grade_point)
            gpa_array.append(weighted_gp)
        elif weighted.upper() == "U":
            unweighted_gp = credits * grade_point 
            gpa_array.append(unweighted_gp)
        else:
            print(ValueError)

        # print
        
        print(f"Class {enter}: {weight} {name.lower()}, Credits: {credits}, Grade: {grade.upper()} ({grade_point})") # Prints class info
get_grade()
# final
GPA = (sum(gpa_array)) / (sum(credit_values))
print(f"GPA: {round(GPA, 2)}")
