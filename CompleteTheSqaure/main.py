# NOTES: Sometimes, numbers will be represented in weird decimals. E.g. 0.1100000000000000005 Unfortunately, that seems to be unavoidable --> "https://stackoverflow.com/questions/57143768/python-is-producing-weird-decimals-when-multiplying" and is caused by internal representation of numbers in Python.

def complete_square(A,B,C):
    if A == 0:
        print("\n\nA cannot be 0!")
        return
    print("\n\nYour equation: y = " + str(A) + "x^2 + " + str(B) + "x + " + str(C))
    
    # Making sure that the coefficient of x^2 is 1.
    print("\nMaking sure that the coefficient of x^2 is 1, and placing a common factor to ensure it is 1.")
    coeff_x = B/A
    print(str(A) + "(x^2 + " + str(coeff_x) + "x + " + str(C/A) + ")")
    
    # Identify the coefficient of x, make it half and square the resultant number.
    print("\nIdentify the coefficient of x, make it half and square the resultant number.")
    resultant_num = round(pow(coeff_x/2,2),2)
    print("(" + str(coeff_x) + " / 2)^2 = (" + str(coeff_x/2) + ")^2 = " + str(resultant_num))
    
    # Add and subtract the above number after the x term in the expression.
    print("\nAdd and subtract the above number after the x term in the expression.")
    print(str(A) + "(x^2 + " + str(coeff_x) + "x + " + str(resultant_num) + " - " + str(resultant_num) + " + " + str(C/A) + ")")
    
    # Factorize the perfect square trinomial formed by the first 3 terms using the suitable identity.
    print("\nFactorize the perfect square trinomial formed by the first 3 terms using the suitable identity.")
    if coeff_x > 0:
        print("In this case, we can use x^2 + 2xy + y^2 = (x + y)^2.")
        print(str(A) + "[(x + " + str(resultant_num ** 0.5) + ")^2 - " + str(resultant_num) + " + " + str(C/A) + "]")
    elif coeff_x < 0:
        print("In this case, we can use x^2 - 2xy + y^2 = (x - y)^2.")
        print(str(A) + "[(x - " + str(resultant_num ** 0.5) + ")^2 - " + str(resultant_num) + " + " + str(C/A) + "]")

    # Simplify the last two numbers.
    print("\nSimplify the last two numbers.")
    last_num = -resultant_num + C/A
    if coeff_x > 0:
        print(str(A) + "[(x + " + str(resultant_num ** 0.5) + ")^2 + " + str(last_num) + "]")
    elif coeff_x < 0:
        print(str(A) + "[(x - " + str(resultant_num ** 0.5) + ")^2 + " + str(last_num) + "]")
    
    # Distribute the outside number.
    print("\nDistribute the outside number.")
    if coeff_x > 0:
        result = str(A) + "(x + " + str(resultant_num ** 0.5) + ")^2 + " + str(round(last_num*A,2))
    elif coeff_x < 0:
        result = str(A) + "(x - " + str(resultant_num ** 0.5) + ")^2 + " + str(round(last_num*A,2))
    print(result)
    
    # Print the final equation and exit the function.
    print("\nFinal equation: y = " + result)
    return

# Driver's code

complete_square(1,4,7)
complete_square(1,2,-5)
complete_square(0,1,1)