def factor_this(a,b,c):
    import math
    
    if type(a) != int or type(b) != int or type(c) != int: # Prohibits non-integers
        print("a, b and c must be integers!")
        return
    elif a == 0:
        print("a must not be zero!") # Prohibits non-quadratic equations
        return
    
    print("\n\nYour equation: " + str(a) + "x^2" + correct_sign(b) + "x" + correct_sign(c))
    
    if b != 0 and c != 0:
        print("\nFirst, we need to calculate the discriminant.\nThe formula is: b^2 - 4ac") # Calculate the discriminant
        discriminant = pow(b,2) - 4 * a * c
        print("The discriminant is " + str(discriminant) + ".")
    
        if discriminant < 0: # Determines if the quadratic equation is factorable over real numbers
            print("\nBecause the discriminant is smaller than 0, it isn't possible to factor the quadratic equation over real numbers.")
            return
        elif discriminant >= 0:
            print("\nBecause the discriminant is greater than or equal to 0, it is possible to factor the quadratic equation over real numbers.")

        if not math.sqrt(discriminant).is_integer(): # Determines if the quadratic equation is factorable over integers
            print("\nBecause the discriminant isn't a perfect square i.e. 25, 36, 64 the quadratic equation isn't factorable over integers.")
            return
        else:
            print("\nBecause the discriminant is a perfect square i.e. 25, 36, 64 the quadratic equation is factorable over integers.")
    
        print("\nTo factor the equation, we need to find two numbers in which their sum is equal to b and their product is equal to a multiplies with c.")
        total = b
        product = a * c
        print("\nThe product is " + str(product) + " and the sum is " + str(total) + ".")
        m = 0
        n = 0
        for i in range(min(-1 * product, product),max(-1 * product, product)):
            if i == 0: # Prevents ZeroDivisionError
                continue
            m = i
            n = product / i

            if n % 1 == 0: # Eliminates .0 while keeping others e.g 2.0 -> 2 , 2.4 -> 2.4
                n = int(n)
            else:
                n = float(n)

            if type(n) == int: # Shows n if it is an integer
                print(str(m) + "*" + str(n) + "=" + str(product) + " / " + str(m) + "+" + str(n) + "=" + str(m+n))
            if m + n == total:
                m = int(m)
                n = int(n)
                break
        print("The two numbers (m,n) that match the requirements are: " + str(m) + " and " + str(n) + ".")
    
        print("\nNext, we separate bx with mx and nx.") # Separates b to two numbers
        print(str(a) + "x^2" + correct_sign(m) + "x" + correct_sign(n) + "x" + correct_sign(c))
    
        print("\nThen, we find the G.C.D (Greatest Common Divisor) of the first two terms and the last two terms and factor them.") # Finds GCF and factor the two terms
        first_gcd = math.gcd(a,m)
        second_gcd = int(n/a*first_gcd) # The integer function is to eliminate .0 e.g. 2.0, 15.0
        common_term = "(" + str(int(a/first_gcd)) + "x" + correct_sign(int(m/first_gcd)) + ")"
        print(str(first_gcd) + "x" + common_term + correct_sign(second_gcd) + common_term) 
    
        print("\nFinally, factor all the terms.") # Factors all the terms
        if "(" + str(first_gcd) + "x" + correct_sign(second_gcd) + ")" == common_term:
            print(common_term + "^2")
        else:
            print("(" + str(first_gcd) + "x" + correct_sign(second_gcd) + ")" + common_term)
    elif b == 0:
        print("\nWe need to find the G.C.D (Greatest Common Divisor) of a and c. ")
        gcd = math.gcd(a,c)
        print(str(gcd) + "(" + str(int(a/gcd)) + "x^2" + correct_sign(int(c/gcd)) + ")")
    elif c == 0:
        print("\nWe need to find the G.C.D (Greatest Common Divisor) of a and b. ")
        gcd = math.gcd(a,b)
        print(str(gcd) + "x" + "(" + str(int(a/gcd)) + "x" + correct_sign(int(b/gcd)) + ")")
    return

def correct_sign(x): # This function checks and returns appropriate sign in front of the numbers
    if x < 0:
        return str(x)
    elif x == 0:
        return ""
    else:
        return "+" + str(x)

'''factor_this(3,17,10)
factor_this(1,-6,9)
factor_this(112,0,56)
factor_this(3,0,48)
factor_this(12,-20,0)
factor_this(462,1386,0)'''
factor_this(-3,-12,5)