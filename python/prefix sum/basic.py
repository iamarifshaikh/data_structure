def prefixSum():
    array = [1]
    runningSum = [0] * len(array)
    runningSum[0] = array[0]
    length = len(array)
    print("Heres the length",length)

    for i in range(length):
        runningSum[i] = runningSum[i - 1] + array[i]

    print(runningSum)
    return runningSum

prefixSum()