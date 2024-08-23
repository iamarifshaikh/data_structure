def check_prime(number):
    if number % 2 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    number = int(input("Enter Number:"))
    if check_prime(number):
        print(number,"is a prime number")
    else:
        print(number,"is not a prime number")
        
        