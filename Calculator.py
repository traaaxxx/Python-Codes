# program to design a simple calculator

while True:
    print("------- Operations -------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your desired choice (1/2/3/4/5) - "))
    print()
    num1 = float(input("Enter the first integer: "))
    num2 = float(input("Enter the second integer: "))
    print()

    match choice:
        case 1:
            result = num1 + num2
            print("The sum of", num1, "and", num2, "is", result)

        case 2:
            result = num1 - num2
            print("The difference of", num1, "and", num2, "is", result)

        case 3:
            result = num1 * num2
            print("The product of", num1, "and", num2, "is", result)

        case 4:
            result = num1 / num2
            print("The quotient of", num1, "and", num2, "is", result)

        case 5:
            break

    new = input("You want to perform another calculation? (Yes/No): ")
    print()
    if new == 'No':
        print("Exiting...")
