# Python Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
            self.length += 1

    def pop(self):
        if self.head is None:
            self.length = 0
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1

    def popfirst(self):
        if self.head is None:
            self.length = 0
            return None
        else:
            temp = self.head.next
            self.head = temp
            self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length:
            print("Enter a valid Index")
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        print("The Value is", temp.data)
        return temp.data

    def set(self, index, value):
        if index < 0 or index >= self.length:
            print("Enter a valid Index")
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.data = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Enter a valid Index")
            return False
        elif index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Enter a valid Index")
            return False
        elif index == 0:
            self.popfirst()
            return True
        elif index == self.length - 1:
            self.pop()
            return True
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
            return True

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print("")


