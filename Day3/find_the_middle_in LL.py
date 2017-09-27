class node:
	def __init__(self,val):
		self.key = val
		self.next = None

def middle(root):
	slow = root
	fast = root
	while fast.next != None and fast != None:
		fast = fast.next.next
		slow = slow.next
	print slow.key

root = node(2)
root.next = node(2)
root.next.next = node(6)
root.next.next.next = node(4)
root.next.next.next.next = node(5)

middle(root)
