import math

def extract_digit(number):
    digit = []
    
    while number > 0:
        last_digit = number % 10
        digit.append(last_digit)
        number = math.floor(number / 10)
    digit.reverse()
    return digit  # Reverse the list to get the digits in ascending order

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    print("Extracted Digits:", end=" ")
    digits = extract_digit(number)
    for num in digits:
        print(num, end=",")
    print()
    