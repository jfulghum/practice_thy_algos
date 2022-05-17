/*
Find smallest positive value in BT



Find most frequent value in binary tree



Count the number of times a target value is in the BT



/**
[4, 2, 1,]
            => 1
      4
    1. 
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

// post order = left, right, current


function mostFreq(node){
  let freq = new Map()
  let mostFreqKey = null
  let maxOccurance = -Infinity
  visit(node)
  
  function visit(node){
    if(!node) return 
    visit(node.left)
    visit(node.right)
    const count = (freq.get(node.val) || 0) + 1

    if(count > maxOccurance) {
      mostFreqKey = node.val
      maxOccurance = count
    }
    freq.set(node.value, count)
  }

  return mostFreqKey
}

console.log(mostFreq(new TreeNode(-10, new TreeNode(3, new TreeNode(3, new TreeNode(-10))))),3)
console.log(mostFreq(new TreeNode(4, new TreeNode(4, new TreeNode(4)))), 4)

const sampleTree = new TreeNode(4, new TreeNode(4), new TreeNode(4, new TreeNode(-1), new TreeNode(-5)))
console.log(mostFreq(sampleTree))


console.log(mostFreq(new TreeNode(3, new TreeNode(-7, new TreeNode(-7)), new TreeNode(5))))

console.log(mostFreq(null))
console.log(mostFreq(new TreeNode(-100)))
