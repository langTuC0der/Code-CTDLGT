#Khoi tao lop Listnode
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None

    def Prenode(self, data):
        newnode = ListNode(data)
        newnode.next = self.head
        self.head = newnode

    def searchnode(self, target):
        curnode = self.head
        while curnode is not None and curnode.data != target:
            curnode = curnode.next
        if curnode is not None:
            print("Tim thay" ,target,"trong danh sach")
        else:
            print("Khong tim thay", target,"trong danh sach")

    def printds(self):
        curnode = self.head
        while curnode is not None:
            print(curnode.data, end=" ")
            curnode = curnode.next

    def removenode(self, target):
        prevnode = None
        curnode = self.head
        while curnode is not None and curnode.data != target:
            prevnode = curnode
            curnode = curnode.next

        if curnode is not None:
            if curnode is self.head:
                self.head = curnode.next
            else:
                prevnode.next = curnode.next
        else:
            print("Khong tim thay", target, "de xoa")


if __name__ == "__main__":
    llist = DSLK
    n = int(input("Nhập số phần tử của danh sách: "))
    # Nhập giá trị và chèn vào đầu danh sách
    for i in range(n):
        print("Nhập thông tin phần tử thứ", i + 1)
        value = int(input())
        llist.Prenode(value)
    llist.printds()