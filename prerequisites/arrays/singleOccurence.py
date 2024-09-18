def singleOccurence(array):
    n = len(array)

    for i in range(n):
        num = array[i]
        count = 0

        for j in range(n):

            if array[j] == num:
                count += 1
        
        # If the occurrence is 1, return the number:
        if count == 1:
            return num

    # This line will never execute if the array contains a single element.
    return -1            

if __name__ == "__main__":
    array = [2,1,1,2,3,3,4]
    answer = singleOccurence(array)
    print(f"The single element is: {answer}")