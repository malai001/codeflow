
class tree:
	def __init__(self,val):
		self.key = val
		self.left = None
		self.right = None

def isum(root):
	if root == None:
		return 0
	return isum(root.left)+root.key+isum(root.right)

def sumtree(root):
	if root == None or root.left == None or root.right == None:
		return 1

	ls = isum(root.left)
	rs = isum(root.right)
	print ls,rs,root.key

	if (root.key == ls+rs and sumtree(root.left) and sumtree(root.right)):
		return 1
	return 0	

root = tree(52)
root.left = tree(10)
root.right = tree(16)
root.left.left = tree (5)
root.left.right = tree(5)
#root.right.right = tree(6)
root.right.left = tree(10)
root.right.right = tree(6)

print sumtree(root)