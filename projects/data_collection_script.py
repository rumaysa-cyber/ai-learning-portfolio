# Welcomes the user to the program:

print("Welcome! Please enter your information as directed below:\n")

# Data collection code starts here:

name = input("Please enter your name: \n")
age = int(input("Please enter your age: \n"))
occupation = input("Please enter your occupation: \n")
height = float(input("Please enter your height in inches: \n"))
is_married = bool(int(input("Are you married? Enter 0 for no and 1 for yes: \n")))
pet_owner = bool(int(input("Do you have a pet? Enter 0 for no and 1 for yes: \n")))
nationality = input("Please enter your nationality: \n")

# Data display code starts here:

print("\nThank you! Please make sure your data is correct:\n")
print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)
print("Height:", height)
print("Is married:", is_married)
print("Pet owner:", pet_owner)
print("Nationality:", nationality)
