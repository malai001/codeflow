class node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

def sumpath(root,s):
	if root is None:
		return (s==0)
	else:
		ans = 0
		subs = s-root.val
		if subs == 0 and root.left == None and root.right == None:
			return 1
		else:
			if root.left !=None:
				ans = ans or sumpath(root.left,subs)
			if root .right != None:
				ans = ans or sumpath(root.right,subs)
	return ans

root = node(1)
root.left = node(2)
root.right = node(3)
s = 3
print sumpath(root,s)