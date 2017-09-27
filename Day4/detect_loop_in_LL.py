class list:
	def __init__(self,val):
		self.key  = val
		self.next = None

def isLoop(root):
	slow = root.next
	fast = slow.next.next

	while fast != None and fast.next != None:
		if slow == fast:
			return True
		else:
			slow = slow.next
			fast = fast.next.next
	return False

root = list(2)
root.next = list(3)
root.next.next = list(4)
root.next.next.next = list(5)
root.next.next.next.next = list(6)
root.next.next.next.next.next = root.next.next

print isLoop(root)