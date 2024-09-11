def extractingDigits(number):
    answer = []
    
    while number > 0:
        last_digits = number % 10
        
        answer.append(last_digits)
        
        number = number // 10
        
    answer.reverse()
    
    return answer

if __name__ == '__main__':
    number = 21892
    result = extractingDigits(number)
    print(result)