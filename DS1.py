stack = []  # empty stack
max_size = 5

def push(element):
    if len(stack) == max_size:
        print("Stack Overflow! Cannot push", element)
    else:
        stack.append(element)
        print(element, "pushed into stack")

def pop():
    if not stack:
        print("Stack Underflow! No element to pop")
    else:
        print("Popped element:", stack.pop())

def display():
    if not stack:
        print("Stack is empty")
    else:
        print("Stack elements are:", stack)

# Driver code
push(10)
push(20)
push(30)
display()
pop()
display()
