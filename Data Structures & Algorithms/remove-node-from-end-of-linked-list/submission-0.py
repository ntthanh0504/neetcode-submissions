class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Tạo một nút dummy đứng trước head để tránh mất dấu đầu danh sách
        dummy = ListNode(0)
        dummy.next = head
        
        # Dùng kỹ thuật 2 con trỏ: fast và slow
        first = dummy
        second = dummy

        # Bước 1: Cho con trỏ 'first' đi trước n + 1 bước
        for _ in range(n + 1):
            first = first.next

        # Bước 2: Dịch chuyển cả 'first' và 'second' cùng lúc với tốc độ như nhau
        # Khi 'first' chạm đến None (cuối danh sách), 'second' sẽ dừng lại ngay TRƯỚC nút cần xóa
        while first is not None:
            first = first.next
            second = second.next

        # Bước 3: Xóa nút bằng cách thay đổi liên kết .next của 'second'
        # Nút bị xóa sẽ là second.next
        second.next = second.next.next

        # Trả về dummy.next (đây chính là đầu danh sách sau khi đã xóa nút)
        return dummy.next