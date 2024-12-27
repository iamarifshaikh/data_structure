import math

def check_prime(num):
    counter = 0
    
    for i in range(1,int(math.sqrt(num)) + 1):
        # If n is divisible by i without any remainder.
        if num % i == 0:
            counter += 1
            
            # if num is not a perfect square count its reciprocal factor
            if num // i != i:
                counter += 1
        
    if counter == 2:
        # Return true, indicating that the number is prime.
        return True
    # If the number of factors is not 2
    else:
        # Return false, indicating that the number is not prime.
        return False        

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    isPrime = check_prime(num)
    if isPrime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")