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

# number = int(input())
# count = 0
# while number:
#     last_digit = number % 10
#     for i in range(2, (last_digit ** 0.5)+ 1):
#         if (last_digit%i==0):
#             count = count + 1
#         else:
#             print(f"{i} is not a prime")
#     number = number // 10

# print(count)


# class aiml:
#     def qwe(self):
#         print("hi")

# class eee:
#     def qwe(self):
#         print("hellp")

# class cse(eee,aiml):
#     def qwe1(self):
#         print("hey")

# a = aiml()
# b = eee()
# c = cse()

# c.qwe()


# class aiml:
#     def __init__(self,u,v):
#         self.x = 10
#         self.y=v
#     def qwe(self,x):
#         print("hi",self.x+b.y)

# a = aiml(10,20)
# b = aiml(30,60)
# a.qwe()
# b.qwe()


# class aiml:
#     def __init__(self,u,v):
#         self.x = u
#         self.y=v
#     def qwe(self,t):
#         print("hi",self.x+b.y,t)

# a = aiml(10,20)
# b = aiml(30,60)
# a.qwe(50)
# b.qwe(40)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def display():
#     temporary = head
#     while temporary is not None:
#         print(temporary.data)
#         temporary = temporary.next
#     print()

"""
def sumOfLinkedList():
    temporary = head
    sum = 0
    while temporary is not None:
        sum += temporary.data
        temporary = temporary.next
    print(f"The sum of all the node data is {sum}")
"""
# def sumOfOdd():
#     temporary = head
#     sum = 0
#     while temporary is not None:
#         if temporary.data % 2 != 0:
#             sum += temporary.data
#         temporary = temporary.next
#     print(f"The sum of all the odd data is {sum}")

# def findMiddleOfNode():
#     fast = slow = head

#     while fast!= None and fast.next!=None:
#         slow = slow.next
#         fast = fast.next.next

#     print(slow.data)

# def evenOrOdd():
# temporary = head
# count = 0
# while temporary!=None:
#     temporary = temporary.next
#     count += 1
# print("It is even" if count%2==0 else "It is odd")

# fast = head
# while fast is not None and fast.next is not None:
#     fast= fast.next.next
# print("It is even" if fast == 0 else "It is Odd")

# head  = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# head.next.next.next.next.next = Node(60)
# display()
# sumOfLinkedList()
# sumOfOdd()
# findMiddleOfNode()
# evenOrOdd()

# class node:
#     def __init__(self, u):
#         self.data = u
#         self.next = None


# def display():
#     t = head
#     while t != None:
#         print(t.data, end=" ")
#         t = t.next


# def reverse(x):
#     p = None
#     c = x
#     while c != None:
#         n = c.next
#         c.next = p
#         p = c
#         c = n
#     return p


# def nthnode(n):
#     f = head
#     s = head
#     while n:
#         f = f.next
#         n = n - 1
#     while f != None:
#         t = s
#         s = s.next
#         f = f.next
#     print(s.data)
#     t.next = reverse(s)


# def add_back(x):
#     t = head
#     while t.next != None:
#         t = t.next
#     t.next = node(x)


# head = node(10)
# add_back(20)
# add_back(30)
# add_back(40)
# add_back(50)
# add_back(60)
# add_back(70)
# add_back(80)
# add_back(90)
# display()
# print()
# nthnode(5)
# display()
# def removeElements():
#     nums = [0, 1, 2, 2, 3, 0, 4, 2]
#     value = 2
#     index = 0
#     for i in nums:
#             if i != value:
#                 nums[index] = i
#                 index += 1
#     return index

# removeElements()


def wrap(n, min_val, max_val):
    return (n - min_val) % (max_val - min_val + 1) + min_val

# Testing the function
print(wrap(6, 1, 5))  # Output: 1
print(wrap(7, 1, 5))  # Output: 2
print(wrap(0, 1, 5))  # Output: 5
print(wrap(-1, 1, 5))  # Output: 4
