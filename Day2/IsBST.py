class node:
	def __init__(self,val):
		self.key = val
		self.left = None
		self.right = None

def isBST(root, left = None, right = None):

	if root == None:
		return True
	if left != None and left.key>root.key:
		return False
	if right != None and right.key<root.key:
		return False
	return isBST(root.left,left,root) and isBST(root.right,root,right)

root = node(4)
root.left = node(2)
root.left.left = node(1)
root.right = node(5)
root.left.right = node(3)

print isBST(root)