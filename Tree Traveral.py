class Node:
  def __init__(self, item):
    self.left = None
    self.right = None
    self.val = item

def inOrder(root):
  if root:
    #traverse left
    inOrder(root.left)
    #traverse root
    print(str(root.val) + "->", end="")
    #traverse right
    inOrder(root.right)

def preOrder(root):
  if root:
    print(str(root.val) + "->", end="")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
  if root:
    postOrder(root.left)
    postOrder(root.right)
    print(str(root.val) + "->", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In order: ")
inOrder(root)
print("\n\npreOrder: ")
preOrder(root)
print("\n\npost order")
postOrder(root)