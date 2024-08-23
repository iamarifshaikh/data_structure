def allDivisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    divisor = allDivisors(number)
    print(" -> ".join(map(str, divisor)))