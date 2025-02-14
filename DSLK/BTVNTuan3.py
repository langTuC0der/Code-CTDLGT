class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class DSLK:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def Len(self):
        return self.size
    def insert_first(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode
        if self.size == 0:
            self.tail = newNode
        self.size += 1
    def insert(self, pos, value):
        if pos < 0 or pos > self.size:
            return
        newNode = ListNode(value)
        if pos  == 0:
            newNode.next = self.head
            self.head = newNode
            if self.size == 0:
                self.tail = newNode
        else:
            predNode = None
            curNode = self.head
            for _ in range(pos):
                predNode = curNode
                curNode = curNode.next
            predNode.next = newNode
            if newNode.next is None:
                self.tail = newNode
        self.size += 1
    def apppen(self, value):
        newNode = ListNode(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.size += 1
    def delete(self, pos):
        predNode = None
        curNode = self.head
        for _ in range(pos-1):
            predNode = curNode
            curNode = curNode.next
        if curNode is self.head:
            self.head = curNode.next
        else:
            predNode.next = curNode.next
        self.size -= 1
    def delete_value(self, value):
        preNode = None
        curNode = self.head
        while curNode is not None and curNode.data != value:
            preNode = curNode
            curNode = curNode.next
        if curNode is self.head:
            self.head = curNode.next
        else:
            preNode.next = curNode.next
        self.size -= 1
    def print(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next
if __name__ == "__main__":
    li = DSLK()
    n = int(input("Nhap so phan tu trong mang: "))
    for i in range(n):
        value = int(input())
        li.apppen(value)
    li.delete_value(1)
    li.print();