# program to find factorial of an integer

def factorial(n):
    fact = 1
    if n < 0:
        print("Factorial of Negative Integers doesn't exist...")

    else:
        for i in range(1, n + 1):
            fact = fact * i
        print("Factorial of", n, "is", fact)


num = int(input("Enter an Integer - "))
factorial(num)
