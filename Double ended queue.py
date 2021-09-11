class DEQueue:
  def __init__(self):
    self.items = []
  
  def isEmpty(self):
    return self.items == []

  def addRear(self, item):
    self.items.append(item)

  def addFront(self, item):
    self.items.insert(0, item)
  
  def removeFront(self):
    self.items.pop(0)

  def removeRear(self):
    self.items.pop()

  def size(self):
    return len(self.items)

  def printQueue(self):
    print(self.items)

d = DEQueue()
print(d.isEmpty())
d.addRear(1)
d.addRear(2)
d.addRear(3)
d.addRear(4)
d.printQueue()
d.removeFront()
d.removeRear()
d.printQueue()