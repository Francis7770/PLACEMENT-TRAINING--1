class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        current = head
        prev = ListNode() 
        prev.val = None
        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else :
                prev = current
                current = current.next
        return head
