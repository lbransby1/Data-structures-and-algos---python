class MyCircularQueue():
  def __init__(self, k):
    self.k = k
    self.queue = [None] * k
    self.head = self.tail = -1

# insert and element into the circular queue
  def enqueue(self, data):

    # checks if the queue is full
    if ((self.tail + 1)% self.k == self.head):
      print("the queue is full\n")

    # checks if the queue is empty, changes head and tail to 0 to signify the queue isn't empty, then adds the data
    elif (self.head == -1):
      self.head = 0
      self.tail = 0
      self.queue[self.tail] = data
      print("\n" + str(data) + " was added to the CQueue")

    # adds the data
    else:
      self.tail = (self.tail + 1) % self.k
      self.queue[self.tail] = data
      print("\n" + str(data) + " was added to the CQueue")

# delete an element
  def dequeue(self):
    if (self.head == -1):
      print("the queue is already empty")
    
    elif (self.head == self.tail):
      temp = self.queue[self.head]
      self.head = -1
      self.tail = -1
      print("The queue is now empty, " + temp + " was removed")
      return temp

    else:
      temp = self.queue[self.head]
      self.head = (self.head +1) % self.k
      print("\n"+ str(temp) + " was dequeued")
      return temp

  def printQueue(self):
    if (self.head == -1):
      print ("The cicrular queue is empty")

    elif (self.tail >= self.head):
      for i in range (self.head, self.tail +1):
        print(self.queue[i], end= "")
      print()
    else:
      for i in range(self.head, self.k):
        print(self.queue[i], end="")
      for i in range(0, self.tail +1):
        print(self.queue[i], end="")
      print()

obj = MyCircularQueue(7)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.printQueue()
print(obj.queue[0])

obj.dequeue()
obj.printQueue()


obj.enqueue(6)
obj.printQueue()



