import math

answer = "yes"

while answer == "yes":
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    options = input("Would you like to add, multiply, divide, raise to the power, or find the sqrt? ")

    if options == "add":
        sum = num1+num2
        print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))
    elif options == "subtract":
        difference = num1-num2
        print("The difference between " + str(num1) + " and " + str(num2) + " is " + str(difference))
    elif options == "multiply":
        product = num1*num2
        print("The product of " + str(num1) + " and " + str(num2) + " is " + str(product))
    elif options == "divide":
        quotent = num1/num2
        print("The quotent between " + str(num1) + " and " + str(num2) + " is " + str(quotent))
    elif options == "raise to the power":
        power = pow(num1, num2)
        print(str(num1) + " raised to the power of " + str(num2) + " is " + str(power))
    elif options == "find the sqrt":
        options2 = input("Would you like to square the first or second number? ")
        if options2 == "first":
            square_root = math.sqrt(num1)
            print("The square root of " + str(num1) + " is " + str(square_root))
        elif options2 == "second":
            square_root = math.sqrt(num2)
            print("The square root of " + str(num2) + " is " + str(square_root))
        else:
            print("Please choose the first or second number to square")
    else:
        print("Please choose one of the listed options")

    answer = input("Would you like to do another equation? ")
    if answer == "yes":
        continue
    else:
        break
    