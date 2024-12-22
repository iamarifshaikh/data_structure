def reverse_number(n):
    # reverseNum = 0
    
    # while n > 0:
    #     last_digit = n % 10
    #     reverseNum = (reverseNum * 10) + last_digit
        
    #     n = n // 10
        
    return str(n)[::-1]

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    answer = reverse_number(n)
    print(f"The reverse number for {n} is {answer}")