# Python Version

def PreOrderTraversal(root):

	print(root.val)
	if root.left:
		PreOrderTraversal(root.left)
	if root.right
		PreOrderTraversal(root.right)
	return

def InOrderTraversal(root):

	if root.left:
		InOrderTraversal(root.left)
	print(root.val)
	if root.right
		InOrderTraversal(root.right)
	return

def PostOrderTraversal(root):

	if root.left:
		PostOrderTraversal(root.left)
	if root.right:
		PostOrderTraversal(root.right)
	print(root.val)
	return

