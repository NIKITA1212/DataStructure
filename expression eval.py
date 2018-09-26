def eval(post):
    operator = ["*", "/", "+", "-"]
    e = list()
    for x in post:
        if x not in operator:
            e.append(x)
        else:
            op2 = e.pop()
            op1 = e.pop()
            e.append(eval1(x ,op1,op2))

    return e[0]

def infitopostfix(exp):

    operator =["*","/","+","-"]
    operand =list()
    stack = list()
    dict = {'*':2,"/":2,"-":1,"+":1}
    a = exp.split()
    #print(a)
    b = len(a)
    for x in a :
        if x not in operator :
            operand.append(x)
        else:
            if not stack:
                stack.append(x)
            #          print(stack)
            else:
                if dict[stack[-1]] >= dict[x]:
                    operand.append(stack.pop())
                    stack.append(x)

                else:
                    stack.append(x)
    while len(stack)>0:
        operand.append(stack.pop())


    return eval(operand)


def eval1(op,op1,op2):

    if op == "+":
        return int(op1)+int(op2)
    if op == "-":
        return int(op1)-int(op2)
    if op == "*":
        return int(op1) * int(op2)
    if op == "/":
        return int(op1)// int(op2)

p = infitopostfix("1 * -2 + -3 * 4")
print(p)
p = infitopostfix("1 + 135 / 134")
print(p)
p = infitopostfix("-234")
print(p)
#print(eval(p))
