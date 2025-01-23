def greatestCommonDivisor(n1,n2):
    while n1 > 0 and n2 > 0:
        # If n1 is greater than n2, subtract n2 from n1 and update a
        if n1 > n2:
            n1 = n1 % n2

        # Else if n2 is greater than n1, subtract n1 from n2 and update b
        else:
            n2 = n2 % n1
    # Return the non-zero value as the GCD
    return n1 if n1 > 0 else n2

if __name__ == '__main__':
    n1 = 20
    n2 = 15

    gcd = greatestCommonDivisor(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)