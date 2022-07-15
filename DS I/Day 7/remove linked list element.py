class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        prev = temp

        while(prev.next != None):
            if (prev.next.val == val):
                prev.next = prev.next.next
            else:
                prev = prev.next
        
        return temp.next