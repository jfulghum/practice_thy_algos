// this works in JS but not in Python b/c every time you call this function in Python, 
// b/c you have the array as the default [] its a mutable object and it will keep the old stuff from the old function call and mess everything up

function findOnlyChildren(root, result = []) {
  if (!root) return;

  if (root.right == null && root.left) {
    result.push(root.left.value);
  }
  if (root.left == null && root.right) {
    result.push(root.right.value);
  }
  findOnlyChildren(root.left, result);
  findOnlyChildren(root.right, result);
  return result;
}
