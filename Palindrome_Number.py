# program to check for a Palindrome Number
def palindrome(a):
    reverse = 0
    temp = a
    while a != 0:
        remainder = a % 10
        reverse = reverse * 10 + remainder
        a //= 10

    if temp == reverse:
        print(temp, "is a Palindrome Number")
    else:
        print(temp, "ain't a Palindrome Number")


num = int(input("Enter a three digit positive integer - "))
palindrome(num)
