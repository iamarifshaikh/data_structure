def reverseString():
    s = ["h", "e", "l"," ", "l", "o"]
    length = len(s) // 2 
    print(f"Length: ",length)
    j = 0

    print(s)
    for i in range(len(s) - 1, length - 1, -1):
        s[i],s[j] = s[j],s[i]
        print(j,i)
        j += 1
        print(s)
        
    # i = len(s) - 1  # Right pointer

    # while j < i:  # Stop when they meet or cross
    #         s[i], s[j] = s[j], s[i]  # Swap elements
    #         j += 1  # Move forward
    #         i -= 1  # Move backward
        
    # print(s)  # Just for checking output    

reverseString()
