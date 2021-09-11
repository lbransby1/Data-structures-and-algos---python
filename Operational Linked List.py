class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

# insert at beginning
  def insertAtBeginning(self, new_data):
    new_node = Node(new_data)                     #creates new node

    new_node.next = self.head                     
    self.head = new_node                          #sets new node as head

# insert after
  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("The given previous node must be in linkedlist")
      return

    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

# insert at end
  def insertAtEnd(self, new_data):
    new_node = Node(new_data)

    if self.head is None:                         #only occurs if linked list is empty
      self.head = new_node
      return  

    last = self.head
    while (last.next):
      last = last.next
    last.next = new_node

# deleting a node
  def deleteNode(self, position):                #position is base 0
    if self.head is None:
      return
    
    temp = self.head

    if position == 0:                            #deletes the head node, and makes the next node the head
      self.head = temp.next
      temp = None
      return

    for _ in range(position - 1):
      temp = temp.next
      if temp is None:
        break

    if temp is None:
      return
    
    if temp.next is None:
      return

    next = temp.next.next
    temp.next = None
    temp.next = next

# print linked list
  def printList(self):
    temp = self.head
    while (temp):
      print(str(temp.data) + "", end="")
      temp = temp.next

# search element
  def search(self, key):
    current = self.head
    while current != None:
      if current.data ==key:
        return True

      current = current.next

    return False

# sort linked list
  def sortLinkedList(self, head):
    current = head
    index = Node(None)

    if head is None:
      return
    else:
      while current != None:
        index = current.next
        while index != None:
          if current.data > index.data:
            current.data, index.data = index.data, current.data
          index = index.next
        current = current.next

# testing
llist = LinkedList()
llist.insertAtEnd(1)
llist.insertAtBeginning(2)
llist.insertAtBeginning(3)
llist.insertAtEnd(4)
llist.insertAfter(llist.head.next, 5)

print('linked list:')
llist.printList()

print("\nAfter deleting element at position 3:")
llist.deleteNode(3)
llist.printList()

print()
item_to_find = 9
if llist.search(item_to_find):
  print(str(item_to_find) + " is found")
else:
  print(str(item_to_find) + " is not found")


print("Sorted List: ")
llist.sortLinkedList(llist.head)
llist.printList()

print()
llist.deleteNode(0)
print("deleted first node")
llist.printList()

# list of operations

# insertAtBeginning
# insertAfter
# insertAtEnd
# deleteNode
# search
# printList