a = list(map(int,input().split()))
b = list(map(int,input().split()))

new_list = []

i,j = 0,0

#  In merging two lists

while i < len(a) and j < len(b):
    if a[i] < b [j]:
        new_list.append(a[i])
        i = i + 1
    # elif a[i] > b[j]:
    #     new_list.append(b[j])
    #     j = j +1
    # else:
    #     new_list.append(a[i])
    #     new_list.appned(b[j])
    #     i = i + 1
    #     j = j + 1
    else:
        new_list.append(b[j])
        j=j+1
        

while j < len(b):
    new_list.append(b[j])
    j = j + 1
    
while i < len(a):
    new_list.append(a[i])
    i = i +1
    
print(new_list)