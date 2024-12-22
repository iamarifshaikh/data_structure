def seiveOfEratosthenes(number):
    is_prime = [True] * (number + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(number ** 0.5), 1):
        if is_prime[i]:
            # Mark all multiples of i from i*i onwards as False
            for j in range(i * i, number + 1, i):
                is_prime[j] = False    

    # Printing all the prime numbers
    primes = [ i for i in range (number + 1) if is_prime[i]]
    return primes
        
if __name__ == "__main__":
    number = int(input("Enter The N number to find the prime number till: "))
    print(f"Prime Numbers Up To {number}: {seiveOfEratosthenes(number)}")