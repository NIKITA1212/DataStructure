class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, new_element):
        new_node = Element(new_element)

        if self.head == None:

            self.head = new_node

        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while (current.next):
            print(current.value)
            current = current.next

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.display()

