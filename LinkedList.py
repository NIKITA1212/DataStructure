class Node:
    def __init__(self, data = -1):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()


    def append_end(self, data):
            n = Node(data)
            current = self.head
            while current.next != None:
                    current = current.next
            current.next = n

    def display(self):
        current = self.head
        while (current.next):
            current = current.next
            print(current.data)

    def append_begin(self,val):
        new_node = Node(val)
        current = self.head
        new_node.next = current.next
        current.next = new_node

    def delete_member(self,val):
        current = self.head
        while(current.data != val) :
            prev = current
            current = current.next
        prev.next = current.next
        current.next = None

    def remove_duplicate(self):
        current = second = self.head

        while current is not None:
            while second.next is not None:  # check second.next here rather than second
                if second.next.data == current.data:  # check second.next.data, not second.data
                    second.next = second.next.next  # cut second.next out of the list
                else:
                    second = second.next  # put this line in an else, to avoid skipping items
            current = second = current.next

    def nth_elemet_from_last(self,n):
        length = l.lenth_of_LinkedList()
        k = length - n + 1
        c = 0
        current = self.head
        while c != k :
            c = c + 1
            current = current.next
        return current.data

    def lenth_of_LinkedList(self):
        current = self.head
        count = 0
        while current.next is not None :
            count +=1
            current = current.next
        return count

    def delete_middle_method1(self):
        current = self.head
        count = 0
        k = l.lenth_of_LinkedList()
        if (k%2 != 0):
            mid = int(k/2) +1
        else:
            mid = k/2 +1
        while count != mid and current.next is not None :
            prev = current
            current = current.next
            count += 1
        prev.next = current.next

    def delete_middle_method2(self):
        slow = self.head
        fast = self.head
        while slow.next is not None and fast.next is not None and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next

    def partition(self, x):
        current = self.head
        h1 = l1 = Node(0)
        h2 = l2 = Node(0)

        while current:
            if current.data < x:
                l1.next = current
                l1 = l1.next
            else:
                l2.next = current
                l2 = l2.next
            current = current.next
        l2.next = None
        l1.next = h2.next
        f = h1.next
        if not f:
            return "[]"

        result = ""
        while f:
            result += str(f.data) + ", "
            f = f.next
        return "[" + result[:-2] + "]"

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
l = LinkedList()
l.append_end(10)
l.append_end(4)
l#.append_end(20)
#l.append_end(10)
#l.append_end(3)
#l.append_end(6)
#print("Last Nth Element of the LinkedList" ,l.nth_elemet_from_last(3))
#l.delete_middle_method1()
#l.delete_middle_method2()
#print(l.partition(3))
#l.display()
l.reverse()
#l.display()
#l.append_begin(1)
#l.append_begin(0)
#l.append_begin(10)
#l.display()
#l.delete_member(5)
#l.delete_member(0)
#l.remove_duplicate()
#l.display()

x = [None] *3 *2
x[0] = 10
x[0] = x[0] + 1
print(x[0])
print(x)
"""
l = [2,4,6]
l = map(str,l)
l1= "".join(l)
m= [2,4,2]
m = map(str,m)
m1= "".join(m)
print(int(l1)+int(m1))
"""