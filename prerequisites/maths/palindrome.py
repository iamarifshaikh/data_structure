def palindrome(number):
    reverseNum = 0
    duplicate = number
    
    while number > 0:
        last_digits = number % 10
        reverseNum = (reverseNum * 10) + last_digits
        number = number // 10 
    
    if reverseNum != duplicate:
        return False
    else:
        return True

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")