class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, value):
        new_node = node(value)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while (current.next):
            current = current.next
            print(current.data)

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)

l.display()



