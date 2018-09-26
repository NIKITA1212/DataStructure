def reverse(s):
    str = ""
    for x in s:
        str = x+str

    return str
print(reverse("123"))

def reverse1(s):
    if len(s) == 0:
        return s
    else:
        return reverse1(s[1:]) + s[0]

print(reverse1("man"))

# Function to reverse a string
def reverse(string):
    string = string[::-1]
    return string
print(reverse("queen"))



# Python code to reverse a string
# using stack

# Function to create an empty stack. It
# initializes size of stack as 0
def createStack():
    stack = []
    return stack


# Function to determine the size of the stack
def size(stack):
    return len(stack)


# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return true


# Function to add an item to stack . It
# increases size by 1
def push(stack, item):
    stack.append(item)


# Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = createStack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])

    # Making the string empty since all
    # characters are saved in stack
    string = ""

    # Pop all characters of string and put
    # them back to string
    for i in range(0, n, 1):
        string += pop(stack)

    return string


# Driver code
s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print("The reversed string(using stack) is : ", end="")
print(reverse(s))

# Python code to reverse a string
# using reversed()

# Function to reverse a string
def reverse(string):
	string = "".join(reversed(string))
	return string

s = "Geeksfor"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using reversed) is : ",end="")
print (reverse(s))
