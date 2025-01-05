# Initialize variables with name and age
name, age = "Thisara", 22

# Print a formatted string using f-strings
print(f"My name is {name}. I am {age} years old")

# Initialize a variable
x = 5

# Check if x is not equal to 10 and print "YES" if true, otherwise print "NO"
if x != 10:
    print("YES")
else:
    print("NO")

# Initialize a counter variable
i = 1

# Use a while loop to iterate from 1 to 100
while i <= 100:
    # Check if the number is odd
    if i % 2 == 1:
        print(i)  # Print odd numbers
        i += 1    # Increment the counter
    else:
        i += 1    # Increment the counter for even numbers without printing

# Initialize two variables
a = 18
b = 10

# Swap the values of a and b using arithmetic operations
a = b - a  # a now holds the difference between b and a
b = b - a  # b now holds the original value of a
a = a + b  # a now holds the original value of b

# Print the swapped values
print(a)
print(b)

# Set default credentials
username = "root"
password = "pass"

# Prompt user to enter username and password and compare with stored credentials
if username == input("Enter username: ") and password == input("Enter password: "):
    print("Correct")  # Print if credentials are correct
else:
    print("Incorrect")  # Print if credentials are incorrect
