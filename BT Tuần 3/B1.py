# #Em hãy viết chương trình nhập vào n giá trị, mỗi giá trị nhập vào được chèn vào đầu danh sách liên kết và in các giá trị của danh sách.
# 
# Input:
# 
# Giá trị đầu tiên: số phần tử của danh sách
# Các giá trị tiếp theo: giá trị của phần tử cần thêm vào đầu danh sách
# Output:
# 
# các giá trị của danh sách được in theo thứ tự từ nút đầu đến nút cuối

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class DS:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode
    def printl(self):
        curNode = self.head
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next
if __name__ == "__main__":
    li = DS()
    n = int(input())
    for _ in range(n):
        value = int(input())
        li.add(value)
    li.printl()