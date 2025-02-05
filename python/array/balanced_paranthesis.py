string = input()

stack = []

for i in range(len(string)):
    if string[i] in "{[(":
        stack.append(string[i])
    elif len(stack) != 0:
        if string[i] == ")" and string[-1] == "(":
            stack.pop()
        elif string[i] == "]" and string[-1] == "[":
            stack.pop()
        elif string[i] == "}" and string[-1] == "{":
            stack.pop()
    else:
        print(i+1)
        break

if len(stack) == 0:
    print(-1)