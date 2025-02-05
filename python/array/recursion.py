def asd(x):
    if x==6:
        return 0
    # t = asd(x +1)
    # return t + x 
    
    # return asd(x+1) * x
    return asd(x-1) * x



print(asd(2))