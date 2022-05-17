/*
Find smallest positive value in BT



Find most frequent value in binary tree



Count the number of times a target value is in the BT



/**
[4, 2, 1,]
            => 1
      4
    -1 -1 
    n   n

**/

class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function findMin(tree){
  if (tree === null){
    return Infinity
  }
  const leftMin = findMin(tree.left)
  const rightMin = findMin(tree.right)
  if (tree.val > 0){
    return Math.min(tree.val, leftMin, rightMin)
  }
  return Math.min(leftMin, rightMin)
}


console.log(findMin(new TreeNode(-10, new TreeNode(4, new TreeNode(3)))),3)
console.log(findMin(new TreeNode(4, new TreeNode(-4, new TreeNode(-3)))), 4)

const sampleTree = new TreeNode(4, new TreeNode(3), new TreeNode(-100, new TreeNode(-1), new TreeNode(5)))
console.log(findMin(sampleTree))


console.log(findMin(new TreeNode(3, new TreeNode(-1, new TreeNode(-7)), new TreeNode(5))))

console.log(findMin(null))
console.log(findMin(new TreeNode(-100)))
