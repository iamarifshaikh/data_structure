b = list(input())

i = 1

while i < len(b):
    if b[i] == "*":
        b.pop(i)
        b.pop(i-1)
        i = i-2
    i = i+1
print(b)