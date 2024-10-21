# print("Hello World!!")
# print(21)

# 15-10-2024/ TUESDAY.

# Escape sequences "\n" and print statements
# print("Wakanda Forever \nValar Morghulis");

'''
Multi
Line 
Comment
'''

# \" \" Double quotes escape sequence.
# print("\"Legendary\" Escape Sequence.")

# separator: sep
# print("The", 10000, "Ships of Nymeria", sep= "|");

# 19-10-2024/ Saturday.
# Variables

# Creating a list of supercars
supercars = ["Bugatti Chiron", "Koenigsegg Jesko", "Pagani Huayra", "Rimac Nevera"]
print(supercars)

# Accessing the first element
print(supercars[0])  # Output: 'Bugatti Chiron'
# Accessing the last element using negative index
print(supercars[-1])  # Output: 'Rimac Nevera'

# Adding an element using append()
supercars.append("Ferrari SF90")
print(supercars)

# Removing an element by value using remove()
supercars.remove("Pagani Huayra")
print(supercars)

# Removing the last element using pop()
supercars.pop()
print(supercars)

# Getting the first two elements using slicing
first_two = supercars[:2]
print("First Two::",first_two)

# Looping through each car
for car in supercars:
    print("Individual Car::",car)

# Loop through the tuple and print each car with its index (starting index at 1)
for index, car in enumerate(supercars, start=1):
    print(f"{index} {car}.")

# 21-10-2024/ Monday.
# Tuples: (Like Arrays in Js but Tuples are Immutable)
    # Creating a tuple of supercars
supercars = ("Bugatti Chiron", "Koenigsegg Jesko", "Pagani Huayra", "Rimac Nevera")
print("Tuple::",supercars)

# Accessing elements of a tuple
print(supercars[0])  # Output: 'Bugatti Chiron'
print(supercars[-1])  # Output: 'Rimac Nevera'

# Packing a tuple
car_info = ("Bugatti Chiron", 261, "Monaco")

# Unpacking a tuple
car, top_speed, location = car_info
print(car)  # Output: 'Bugatti Chiron'
print(top_speed)  # Output: 261
print(location)  # Output: 'Monaco'


# Dictionaries: (Like Objects in Js) (Everything in Python, is an Object cwh)
# Creating a dictionary with supercars and their top speeds (mph)
supercars = {
    "Bugatti Chiron": 304,
    "Koenigsegg Jesko": 300,
    "Pagani Huayra": 238,
    "Rimac Nevera": 258
}

print("Dictionary::",supercars)

# Accessing the top speed of the Bugatti Chiron
print(supercars["Bugatti Chiron"])  # Output: 304

# Adding a new car and updating an existing one
supercars["Ferrari SF90"] = 211
supercars["Bugatti Chiron"] = 305  # Updating the top speed
print(supercars)

# Removing a key-value pair from the dictionary
del supercars["Pagani Huayra"]
print(supercars)

# Looping through keys and values in a dictionary
for car, speed in supercars.items():
    print(f"{car} has a top speed of {speed} mph.")

# Checking if a key exists in the dictionary
if "Bugatti Chiron" in supercars:
    print("Bugatti Chiron is in the dictionary!")

def get_speed(car_name):
    return supercars.get(car_name, "Car not found")

print(get_speed("Rimac Nevera"))  # Output: 258
print(get_speed("Lamborghini Aventador"))  # Output: Car not found
