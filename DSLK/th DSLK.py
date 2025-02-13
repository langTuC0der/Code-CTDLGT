# tạo DSLK
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# tạo biến
a = ListNode(15)
b = ListNode(63)
c = ListNode(27)
d = ListNode(35)
e = ListNode(50)

# tạo trường next
a.next = b
b.next = c
c.next = d
d.next = e
# duyệt danh sách
def traversal(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next
# tìm kiếm
def unorderedSearch(head, target):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None
# thêm nút 
def append(head, item):
    newNode = ListNode(item)
    newNode.next = head
    head = newNode
def delete(head, target):
    predNode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        predNode = curNode
        curNode = curNode.next
    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            predNode.next = curNode.next
    return head
traversal(a)
a = delete(a, 63)
print("sau khi xoa: ")
traversal(a)