def second_largest_smallest_number(array):
    # Initialize the variable to keep track of largest and second largest numbers.
    largest = second_largest = float('-inf')
    for number in array:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    
    # Intitialize the variable to keep track of smallest and second smallest numbers.
    smallest = second_smallest = float('inf')
    for number in array:
        if number < smallest:  # Found a new smallest
            second_smallest = smallest  # Update second smallest
            smallest = number  # Update smallest
        elif number < second_smallest and number != smallest:
            # Update second smallest only if the current number isn't equal to the smallest
            second_smallest = number
    if second_largest == float('-inf') or second_smallest == float('inf'):
        return "Array does not have disticnt second largest and second smallest numbers" 
    
if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    result = second_largest_smallest_number(array)
    
    if isinstance(result,str):
        print(result)
    else:
        second_smallest, second_largest = result
        print(f'Second largest number: {second_largest}')
        print(f'Second smallest number: {second_smallest}')