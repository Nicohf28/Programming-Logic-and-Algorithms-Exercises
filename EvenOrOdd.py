# EvenOrOdd.py
# This script allows the user to input numbers and tells them whether each number is even or odd.
# It includes input validation and the option to repeat the process.

def get_integer():
    """
    Prompts the user to enter an integer.
    Keeps asking until a valid integer is provided.
    Returns:
        int: The integer entered by the user.
    """
    while True:
        entry = input("-> Enter a number: ")
        try:
            return int(entry)
        except ValueError:
            print("// Error. Please enter an Integer. Try again.")

def is_even(n):
    """
    Checks if a number is even.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

def wants_to_continue():
    """
    Asks the user if they want to enter another number.
    Repeats the prompt until the user inputs a valid option.

    Returns:
        bool: True if the user wants to continue, False otherwise.
    """
    while True:
        print("-> Enter (1) for yes.")
        print("-> Enter (2) for no.")
        option = input("Do you want to enter another number?: ")

        if option == '1':
            print("// Let's do another one!")
            return True
        elif option == '2':
            print("// Goodbye!")
            return False
        else:
            print("// Invalid option. Please enter (1) or (2). Without parentheses.")

def main():
    """
    Main loop of the program.
    Gets numbers from the user, checks if they are even or odd,
    and asks if they want to continue.
    """
    while True:
        number = get_integer()

        # Determine if the number is even or odd
        if is_even(number):
            print("// The number is even.")
        else:
            print("// The number is odd.")

        # Ask the user if they want to try again
        if not wants_to_continue():
            break

# Run the program only if it is executed directly (not imported)
if __name__ == "__main__":
    main()
