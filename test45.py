class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self,L2):
        dummy = Node(0)
        current = dummy
        temp1 = self.head
        temp2 = L2.head
        while temp1 is not None and temp2 is not None:
            if temp1.value < temp2.value :
                current.next = temp1
                temp1 = temp1.next
            else:
                current.next = temp2
                temp2 = temp2.next
            current = current.next

        while temp1 is not None:
            current.next = temp1
            temp1 = temp1.next
        while temp2 is not None:
            current.next = temp2
            temp2 = temp2.next

        return dummy



l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)

l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""