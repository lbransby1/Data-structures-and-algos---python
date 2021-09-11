class Queue:
  def __init__(self):
    self.queue = []

# add an element
  def enqueue(self, item):
    self.queue.append(item)

# remove an element
  def dequeue(self):
    self.queue.pop()  

 #display the queue
  def display(self):
    print(self.queue)

# display size
  def size(self):
    print("The queue is "+ str(len(self.queue)) + " items long")

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()
q.size()

q.dequeue()

print("After removing an element:")
q.display()
q.size()