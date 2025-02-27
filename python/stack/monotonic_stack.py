def monotonic_stack():
    array = [3, 1, 4, 1, 5, 9, 2, 6]
    stack = []
    result = []
    
    for num in array:
        while stack and stack[-1] < num:
            stack.pop()
        
        # Construct the result array
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)
        
        stack.append(num)    
    
    print(result)
    
monotonic_stack()