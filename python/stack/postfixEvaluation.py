expression="3,4,2,-,3,6,2,/,+,*,+"
expression = expression.split(",")
print(expression)

stack = []
def evaluateExpression(expression):
    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                c = b + a
                stack.append(c)
            elif i == "-":
                c = b - a
                stack.append(c)
            elif i == "*":
                c = b * a
                stack.append(c)
            elif i == "/":
                c = b // a
                stack.append(c)
            elif i == "^":
                c = b ^ a
                stack.append(c)
            else:
                print("Something went wrong!")
                break

    print("We got after evaluation is ",stack.pop())

evaluateExpression(expression)