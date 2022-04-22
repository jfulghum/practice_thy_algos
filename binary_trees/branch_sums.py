class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums = []
	calculateBranchSums(root, 0, sums)
	return sums
	

def calculateBranchSums(node, runningSum, sums):
	if node is None:
		return
	
	newRunningSum = runningSum + node.value
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return
	
	calculateBranchSums(node.left, newRunningSum, sums)
	calculateBranchSums(node.right, newRunningSum, sums)
	

	
## this is also correct

def branchSums(root):
	sums = []
	calculateBranchSums(sums, root, 0)
	return sums
	

def calculateBranchSums(sums, node, runningSum):
	if node is None:
		return
	runningSum += node.value
	if node.left is None and node.right is None:
		sums.append(runningSum)
		return
	calculateBranchSums(sums, node.left, runningSum)
	calculateBranchSums(sums, node.right, runningSum)
