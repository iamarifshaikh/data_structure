# n = int(input("Enter the number"))
# x = 1
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j== 0 or j == n -1:
#             print("* ",end="")
#         else:
#             print(x,end=" ")
#             x = x + 1
#     print()

# array =[4,5,6]

# array.append(44)
# array.extend([4,5,5.5])
# array.extend({4,4,5,6,6})
# array.append(44.22)
# print(len(array))


# array =[4,5,6]

# array.extend("hI")
# array.extend("4.5")
# array.append({4,4,8})
# array.extend(45)
# array.append(True)
# print(len(array))

# array = [4, 5, 6]

# array.extend("hI")
# array.extend("4.5")
# array.append({4,4,8})
# array.append(True)
# print(len(array))

# array = [4, 5, 6,7,8]
# array.insert(20,200)
# print(array)


# array = [4, 5, 6, 7,8]
# array.remove(17)
# print(array)

# a={5:6,2:7}
# print(a[3])

# a={5,6,2,7}
# a.clear(8)
# print(a)

# a=[4,5,6,7]
# b=a
# b[0] = 50
# print(a,b)

# a = [4, 5, 6, 7]
# b = a.copy()
# b[0] = 50
# print(a, b)

# a = [4, 5, 6, 7]
# b = a
# b.clear()
# print(a, b)

# a=[4,5,6,7]
# a.sort(reverse=True)
# print(a)


# a=["car","cat","bike","apple"]
# a.sort()
# # This is called lixographical order
# print(a)

# a = ["car", "school", "sTudent", "apples"]
# a.sort()
# # This is called lixographical order
# print(a)

# a = ["car", "school", "sTudent", "apples"]
# a.sort()
# print(a)

# FInd the length of a string

# a=["car","school","hi","apple"]
# b = []

# for i in a:
#     b.append(len(i))
# c=list(zip(b, a))
# print(c)
# c.sort()
# d=[]
# for j in c:
# d.append(i[1])
# print(d)

# a.sort(key=len)
# print(a)

# a=[[3,8],[9,7],[2,1],[4,5]]
# a.sort(key=max)
# print(a)
# def qwe(x):
#      return
# a = [3, 8, 9, 7, 2, 1, 4, 5]
# a.sort(key=min)
# print(a)

# a={5,6,7,7,8,9,21,3}
# a.add(200)
# print(a)

# a = {5, 6, 7, 7, 8, 9, 21, 3}
# b= a.pop()
# print(b)


# difference between discard and remove if a certain valie is not there in discard in it will not gonna create any problem wwhereas in remove it will create a problem and will throw error
# a = {5, 6, 7, 7, 8, 9, 21, 3}
# b=a.remove(7)
# print(a)

# a = {5, 6, 7, 7, 8, 9, 21, 3}
# b=a.discard(7)
# print(b)

# a={4,6,8,9,1}
# b = {5,6,4,2,1}
# c= a.union(b)
# print(c)

# a = {4, 6, 8, 9, 1}
# b = {5, 6, 4, 2, 1}
# c = a.intersection(b)
# print(c)

# a = {4, 6, 8, 9, 1}
# b = {5, 6, 4, 2, 1}
# c = a.difference(b)
# print(c)

# a = {4, 6, 8, 9, 1}
# b = {5, 6, 4, 2, 1}
# c = b.difference(a)
# print(c)

# a = {4, 6, 8, 9, 1}
# b = {5, 6, 4, 2, 1}
# c = a.symmetric_difference(b)
# print(c)


# a = {4, 6, 8, 9, 11,12,14,11}
# b = { 6, 4}
# c = a.issuperset(b)
# print(c)

# array = [4,5,6,7,4,5,67,]

# for i in range(array):
#     pass

#     for j in range(j+1):
#         pass

number = int(input())
count = 0
while number:
    last_digit = number % 10
    for i in range(2, (last_digit ** 0.5)+ 1):
        if (last_digit%i==0):
            count = count + 1
        else:
            print(f"{i} is not a prime")
    number = number // 10
    
print(count)