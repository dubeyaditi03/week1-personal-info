# Personal Information Manager
# First Python Project

# Welcome Message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)

# Static Information
name = "Aditi Dubey"
age = 21
city = "Pune"
hobby = "Singing"

# User Input
print("\nPlease tell me about yourself:")

favorite_food = input("What's your favorite food? ")

while favorite_food == "":
    print("Please enter valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")

while favorite_color == "":
    print("Please enter valid color!")
    favorite_color = input("What's your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display Output
print("\n" + "=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")

print(f"\nFavorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")

# Goodbye Message
print("\n" + "=" * 40)
print("Thanks for using this program!")
print("=" * 40)
