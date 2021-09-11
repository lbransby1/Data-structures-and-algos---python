# creating a stack
def create_stack():
  stack = []
  return stack

# check if stack is empty
def check_empty(stack):
  return len(stack) == 0

# add item to stack
def push(stack, item):
  stack.append(item)
  print("pushed item: " + item)

# pop
def pop(stack):
  if (check_empty(stack)):
    return "Stack is empty"
  return stack.pop()
 
# print stack
def print_stack(stack):
  print(stack)

stack = create_stack()
print("stack is created")
print("Stack empty is: " + str(check_empty(stack)))
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print(str(stack))
print("Stack empty is: " + str(check_empty(stack)))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
