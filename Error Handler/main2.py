numbers = []  # List to store valid numbers

while True:
    try:
        user_input = input("Enter a positive integer greater than 0 (or 0 to stop): ")
        
        # Check if input is a digit (this prevents non-integer input)
        if not user_input.isdigit() and not user_input.startswith('-'):
            raise ValueError("Invalid input! Please enter a positive integer.")
        num = int(user_input)

        # Stop immediately if negative
        if num < 0:
            raise ValueError("Negative number entered. Please inform a positive integer.")

        # Stop asking if zero is entered
        if num == 0:
            break

        numbers.append(num)  # Store valid number
    except ValueError as e:
        print(f"Error: {e}")

# Display all entered numbers and their squares
print("\nNumbers entered and their squares:")
for n in numbers:
    print(f"{n}² = {n**2}")