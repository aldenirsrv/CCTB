numbers = []  # List to store valid numbers

while True:
    try:
        user_input = input("Enter a positive integer greater than 0 (or 0 to stop): ")
        
        # Check if input is a digit (this prevents non-integer input)
        if not user_input.isdigit() and not user_input.startswith('-'):
            raise ValueError(f"Invalid literal for int() with base 10: '{user_input}'!")
        num = int(user_input)

        # Stop immediately if negative
        if num < 0:
            print("- Cannot enter a negative values: '{user_input}'. Stopped!")
            numbers = []
            break

        # Stop asking if zero is entered
        if num == 0:
            break

        numbers.append(num)  # Store valid number
    except ValueError as e:
        print(f"Error: {e}")

if len(numbers) > 0:
    print("\nNumbers entered and their squares:")
    for n in numbers:
        print(f"{n}² = {n**2}")