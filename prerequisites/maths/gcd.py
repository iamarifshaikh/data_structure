def greatestCommonDivisor(n1,n2):
    gcd = 1

    for i in range(1,min(n1,n2)):
        if n1%i==0 and n2%i==0:
            gcd = i
    # Return the greatest
    # common divisor (gcd)
    return gcd 

if __name__ == '__main__':
    n1 = 15
    n2 = 20
    
    gcd = greatestCommonDivisor(n1,n2)

    print("GCD of", n1, "and", n2, "is:", gcd)