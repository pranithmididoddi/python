class Solution(object):
    #find if the linkedlist has a cycle or not
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        p1=head
        p2=head
        while True:
            if p1.next is not None:
                p1=p1.next.next
                p2=p2.next
                if p1 is None or p2 is None:
                    return False
                elif p1==p2:
                    return True
            else:
                return False
        return False