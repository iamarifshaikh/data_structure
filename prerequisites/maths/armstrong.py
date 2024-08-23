def isArmstrong(number):
    digits = len(str(number))
    
    sum = 0
    
    n = number
    
    while n > 0:
        last_digit = n % 10
        sum += last_digit ** digits
        n = n // 10
        
    # Check if the sum of digits raised to
    # the power of k equals the original number
    return sum == number
    
if __name__ == "__main__":
    number = int(input("Enter the number: "))
    if isArmstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")