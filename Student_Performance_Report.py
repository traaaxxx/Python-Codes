# program to design a student performance report

def status(a):
    if 200.00 < a <= 500.00:
        print("Status: Pass")
    else:
        print("Status: Fail")


def grade(b):
    if 450 < b <= 500:
        print("Grade: O")
    elif 400 < b <= 450:
        print("Grade: E")
    elif 350 < b <= 400:
        print("Grade: A")
    elif 300 < b <= 350:
        print("Grade: B")
    elif 250 < b <= 300:
        print("Grade: C")
    elif 200 < b <= 250:
        print("Grade: D")
    else:
        print("Grade: F")


def average(c):
    return c / 5


def percentage(d):
    return d / 5


name = input("Enter the Name - ")
roll = int(input("Enter the Roll Number - "))
print()
print("------- Enter Marks -------")
mark1 = float(input("Mathematics: "))
mark2 = float(input("Physics: "))
mark3 = float(input("Chemistry: "))
mark4 = float(input("Computer Science: "))
mark5 = float(input("English: "))
total = mark1 + mark2 + mark3 + mark4 + mark5
avg = average(total)
percent = percentage(total)
print()
print("----- Student Performance Report -----")
print("Name:", name)
print("Roll Number:", roll)
print("Total Marks Secured: " + "{:.2f}".format(total))
print("Average: " + "{:.2f}".format(avg))
print("Percentage: " + "{:.2f}".format(percent))
grade(total)
status(total)
