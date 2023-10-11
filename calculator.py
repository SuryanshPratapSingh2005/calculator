def calculate(num1, num2, operator):
    """Performs a basic arithmetic operation on two numbers.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The arithmetic operator (+, -, *, or /).

    Returns:
        The result of the operation.
    """

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operator.")


def main():
    """Prompts the user to input two numbers and an operation choice, then performs the calculation and displays the result."""

    print("Welcome to the simple calculator!")

    # Get the user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, or /): ")

    # Perform the calculation
    result = calculate(num1, num2, operator)

    # Display the result
    print("The result is:", result)


if __name__ == "__main__":
    main()
