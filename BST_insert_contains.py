
class BST():
	def __init__(self, value):
		self.value is value
		self.right is None
		self.left is None
		
	def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
				else:
					currentNode = currentNode.left 
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
				else:
					currentNode = currentNode.right 
		return self
	
	def contains(self, value):
		currentNode = self
		if currentNode is not None:
			if currentNode.value = value:
				return True
			elif currentNode.value < value:
				currentNode = currentNode.left
			else:
				currentNode = currentNode.right
		return False
	
		
