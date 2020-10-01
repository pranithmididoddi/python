class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def traverse(self):
		printvalue = self.head
		while printvalue is not None:
			print(printvalue.data)
			printvalue = printvalue.next

	def insertAtBegining(self, head):
		newNode = Node(head)

		# updating the node
		newNode.next = self.head
		self.head = newNode

	def insertAtEnd(self, newNode):
		newNode = Node(5)
		if self.head is None:
			self.head = newNode
			return
		lastnode = self.head
		while (lastnode.next):
			lastnode = lastnode.next
		lastnode.next = newNode
        
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
