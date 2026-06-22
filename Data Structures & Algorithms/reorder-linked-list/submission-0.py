# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Trường hợp danh sách trống hoặc chỉ có 1, 2 nút thì không cần thay đổi
        if not head or not head.next or not head.next.next:
            return

        # Bước 1: Tìm giữa danh sách sử dụng Fast & Slow pointers
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Tách danh sách làm 2 nửa
        second_half_head = slow.next
        slow.next = None

        # Bước 2: Đảo ngược nửa sau của danh sách liên kết
        curr = second_half_head
        prev = None
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        reverse_second_head = prev

        # Bước 3: Trộn đan xen (Merge) trực tiếp tại chỗ (In-place)
        first = head
        second = reverse_second_head

        while second:
            # Lưu lại địa chỉ của các nút tiếp theo trước khi bẻ con trỏ .next
            next_first = first.next
            next_second = second.next

            # Kết nối nút từ nửa đầu sang nửa sau
            first.next = second
            # Kết nối nút nửa sau về nút kế tiếp của nửa đầu
            second.next = next_first

            # Dịch chuyển hai con trỏ chính lên để tiếp tục vòng lặp
            first = next_first
            second = next_second