class ListNode:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.next = None
        self.size = 0
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add_sale(self, item_id, name, price, quantity):
        newNode = ListNode(item_id, name, price, quantity)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    def print_sale(self):
        curNode = self.head
        while curNode is not None:
            print(f"Mã: {curNode.item_id}, Tên: {curNode.name}, Đơn Giá: {curNode.price}, Số lượng: {curNode.quantity}")
            curNode = curNode.next
    def turnover(self, itemID):
        curNode = self.head
        while curNode is not None and curNode.item_id != itemID:
            curNode = curNode.next
        if curNode is not None:
            tur = curNode.price * curNode.quantity
            print(f"Doanh thu của mặt hàng (MS: {curNode.item_id}/{curNode.name}) là: {tur} ")
        else:
            print("Không tìm thấy mặt hàng")
if __name__ == "__main__":
    lk = LinkedList()
    n = int(input("Nhập số lượng mặt hàng: "))
    for i in range(n):
        print(f"Nhập mặt hàng {i+1}: ")
        item_id = input("Nhập mã: ")
        name = input("Nhập tên: ")
        price = float(input("Nhập giá: "))
        quantity = int(input("Nhập số lượng: "))
        lk.add_sale(item_id, name, price, quantity)
    lk.print_sale()
    tur = input("Nhập mặt hàng cần tính: ")
    lk.turnover(tur)
    new = bool(input("Bạn có muốn tính mặt hàng khác nữa không(1/0): "))
    while new == 1:
        tur = input("Nhập mặt hàng cần tính: ")
        lk.turnover(tur)
        if(new!=1):
            break