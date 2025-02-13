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
        li.insert(i, value)
    li.delete(2)
    li.print();