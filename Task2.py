import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Ask the user for complexity level
print("Choose password complexity:")
print("1. Simple (only letters)")
print("2. Medium (letters + numbers)")
print("3. Strong (letters + numbers + symbols)")

choice = input("Enter your choice (1/2/3): ")

# Select characters based on complexity
if choice == '1':
    characters = string.ascii_letters
elif choice == '2':
    characters = string.ascii_letters + string.digits
elif choice == '3':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Using simple by default.")
    characters = string.ascii_letters

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print("\nGenerated Password:", password)
