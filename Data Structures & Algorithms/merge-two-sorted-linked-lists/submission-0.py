# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def log_list(head: Optional[ListNode]) -> str:
    nodes = []
    curr = head
    # Giới hạn 10 node để tránh vòng lặp vô hạn nếu con trỏ bị trỏ vòng lúc debug
    count = 0 
    while curr and count < 10:
        nodes.append(str(curr.val))
        curr = curr.next
        count += 1
    if curr:
        nodes.append("...")
    return "[" + " -> ".join(nodes) + "]"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
