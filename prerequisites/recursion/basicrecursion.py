def recursion(i,number):
    if i > number :
         return  # Base case: stop recursion when i exceeds number
    
    print("Arif Shaikh")
    recursion(i + 1, number)  # Recursive call with incremented i



if __name__ == "__main__":
    number = 15
    recursion(1,number)