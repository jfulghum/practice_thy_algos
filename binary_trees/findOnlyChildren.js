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
