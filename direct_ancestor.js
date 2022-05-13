function directAncestor(head, a, b) {
  let queue = [head]
  while (queue.length){
    let nodeToCheck = queue.shift();
    if (nodeToCheck.value === a){

      if(nodeToCheck.left && nodeToCheck.left.value === b){
        return true;
      } 
      if(nodeToCheck.right && nodeToCheck.right.value === b){
        return true
      }
    } 
    if (nodeToCheck.left){
    queue.push(nodeToCheck.left)
    }
    if (nodeToCheck.right){
    queue.push(nodeToCheck.right)
    }
  }
  return false
}


//a = 2
//b = 9

//       1
//     /   \
//    2     3
//   / \    / \
//  8   5  3   9
// / \
// 9


//TEST CASES

let tree1 = new TreeNode(1, new TreeNode(1), new TreeNode(2, new TreeNode(3), new TreeNode(4)))
let tree2 = new TreeNode(1, new TreeNode(1), new TreeNode(2, new TreeNode(5), new TreeNode(9)))
let tree3 = new TreeNode(1, new TreeNode(3), new TreeNode(2));


console.log(directAncestor(tree1, 3, 4)); //false
console.log(directAncestor(tree2, 1, 9)); //false
console.log(directAncestor(tree3, 1, 2)); //true
