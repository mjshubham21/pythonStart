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

# Typecasting:
# Implicit vs. Explicit Typecasting
# Implicit Typecasting: Automatically done by the interpreter when it can safely convert one type to another. For example, adding an integer to a float will automatically result in a float.
# Explicit Typecasting: Manually converting one data type to another using functions or methods.

# Convert string to integer
speed = "250"
speed_int = int(speed)
print(speed_int)  # Output: 250

# Convert integer to string
car_count = 3
car_count_str = str(car_count)
print("Number of cars: " + car_count_str)  # Output: Number of cars: 3

# Convert list to tuple
cars = ["Bugatti", "Pagani", "Koenigsegg"]
cars_tuple = tuple(cars)
print(cars_tuple)  # Output: ('Bugatti', 'Pagani', 'Koenigsegg')

# 22-10-2024/ Tuesday:
# Getting Input in Python
# In Python, the input() function reads input from the keyboard as a string. If you want to work with other data types (like integers or floats), you'll need to convert the input.

# Getting a string input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

# Getting an integer input
# age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

# Asking user for their favorite supercar
# supercar = input("Enter your favorite supercar: ")
# speed = int(input("Enter the top speed (in km/h): "))

# print(f"Your favorite supercar is {supercar} with a top speed of {speed} km/h!")

# Handling Errors in Input (Python Example)
# In Python, you might want to handle invalid inputs (e.g., the user enters a non-numeric value where a number is expected). You can use try-except to handle such cases.

# try:
    # speed = int(input("Enter the top speed (in km/h): "))
    # print(f"Your car's speed is {speed} km/h!")
# except ValueError:
    # print("Please enter a valid number for the speed.")

st= '''
Multiline strings are
enclosed in triple 
or
dpuble quotes.
'''
# print(st)

# Strings

# Using single or double quotes
car = 'Bugatti'
quote = "The Fast and Furious saga is thrilling!"

# String concatenation
first_part = "Bugatti"
second_part = " is a hypercar."
full_sentence = first_part + second_part
print(full_sentence)  # Output: Bugatti is a hypercar.

# Using f-strings for formatted output
speed = 490.48
message = f"The Bugatti Chiron reached {speed} km/h."
print("String concatination:: ",message)  # Output: The Bugatti Chiron reached 490.48 km/h.

car = "Koenigsegg"
# Slicing the string (start:end)
print("car[0:4]:: ",car[0:4])  # Output: Koen
print("car[4:]:: ",car[4:])   # Output: igsegg (from index 4 to the end)

# Escape Sequences:
# Char  Means           E.G
# \'	Single Quote	'It\'s a supercar'
# \"	Double Quote	"He said, \"Wow!\""
# \\	Backslash	    'C:\\Program Files\\Bugatti'
# \n	Newline	        'Bugatti\nVeyron'

# In Python, you can create raw strings by prefixing a string with r. This tells Python to treat backslashes as literal characters, which is useful when working with file paths or regular expressions.

file_path = r"C:\Program Files\Bugatti"
print(file_path)  # Output: C:\Program Files\Bugatti
