def count_digits(number):
    digit = 0

    while number > 0:
        digit += 1
        number = number // 10
    return digit

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    answer = count_digits(number)
    print(f"The total number of digit is {answer}")