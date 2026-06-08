print("Welcome to the Interactive Personal Data Collector!\n")

# Taking input from user
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Printing data with type and memory address
print("Name:", name, "(Type:", type(name), ", Memory Address:", id(name), ")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height), ")")
print("Favourite Number:", fav_number, "(Type:", type(fav_number), ", Memory Address:", id(fav_number), ")")

# Calculating approximate birth year
birth_year = 2026 - age

print("\nYour birth year is approximately:", birth_year,
      "(based on your age of", age, ")")

print("\nThank you for using the Personal Data Collector. Goodbye!")    