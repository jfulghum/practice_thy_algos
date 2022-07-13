// use 

// runtime disadvatnage 

function helper(node, target) {
  let queue = [node]
  while (queue.length) {
    let node = stack.pop()
    if (node.value == target) {
      return true
    }
    if (node.left) {
      stack.push(node.left)
    }
    if (node.right) {
      stack.push(node.right)
    }
  }
  return false
}


function findDirectParent(tree, a, b) {
  let stack = [tree]
  while (stack.length) {
    let node = stack.pop()
    if (node.val == a) { 
      if((node.left && node.left.val == b) || 
         (node.right && node.right.val == b)) {
        return true
      }
    }
    if (node.left) {
      stack.push(node.left)
    }
    if (node.right) {
      stack.push(node.right)
    }
  }
  return false
}



// TreeNode(1, TreeNode(2))
//      3
//    2   4
//  1 0   5 6
//           7

// 2, 4 -> False
// 2, 0 -> True
// 3, 0 -> True

// 2 5 7

// DFS - xxxxxxxxx <- stack
// BFS - xx <- queue

// Tree equivalent of for loops:

// Recursive DFS
// Iterative DFS
// Iterative BFS


// arr = [1, 2, 3]

*/
/*
     3
   2   4
 1 0   5 6
          7

2, 4 -> False
2, 0 -> True <--
3, 0 -> False

*/
function findDirectParent(tree, a, b) {
  let stack = [tree]
  while (stack.length) {
    let node = stack.pop()
    if (node.val == a) { 
      if((node.left && node.left.val == b) || 
         (node.right && node.right.val == b)) {
        return true
      }
    }
    if (node.left) {
      stack.push(node.left)
    }
    if (node.right) {
      stack.push(node.right)
    }
  }
  return false
