from django.test import TestCase

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)

        self.head = node

    def show(self):
        itr = self.head
        LL = ''
        while itr is not None:
            LL += str(itr.data) + ' -> '
            itr = itr.next

        print(LL)


l = Linked()
l.insert(5)
l.insert(10)

l.show()
