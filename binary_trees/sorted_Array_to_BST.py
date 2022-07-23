/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * Problem: Sorted Array to BST
 * 
 * [-10, -3, 0, 5, 9]
 * 
 *      0
 *     / \
 *   -3    9
 *    /   /
 *  -10   5
 * 
 * 
 * [1, 2, 3, 4]
 * 
 *    2
 *  /  \
 * 1    3 
 *       \
 *        4
 *   
 *    3
 *   /  \
 *   2   4 
 *  / 
 * 1
 * 
 * 1, 3
 * 
 *   3
 *  /
 * 1
 * 
 * 1
 *  \
 *   3
 * 
 * Constraints
 * - height balanced (height of subtrees cannot differ by more than 1)
 * - can be negative or positive
 * - numbers in the array are strictly increasing
 * - array is of reasonable size
 * 
 * Edge cases
 * - even length arrays could have multiple roots
 * - array is of length 0 -> return null
 * 
 * Approach
 * 
 * [-10, -3, 0, 5, 9]
 * 
 *      0
 *     / \
 *   -3    9
 *    /   /
 *  -10   5
 * 
 *      0
 *    -3. 9 
 * 
 * 
 * Main Method
 * - start at the middle value in the array
 * - construct a node with that value
 * 
 * Helper Method
 * - build left subtree recursively with arr[0:mid - 1]
 * - build right subtree recursively with arr[mid + 1:]
 * 
 */

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */

function TreeNode(val, left, right) {
      this.val = (val===undefined ? 0 : val)
      this.left = (left===undefined ? null : left)
      this.right = (right===undefined ? null : right)
}

// Time: O(n)
// Space: O(log n)
 var sortedArrayToBST = function(nums) {
   function helper(left, right) {
     // base case
     if (left > right) {
       return null;
     }

     // find the middle element
     const mid = Math.floor((left + right) / 2);

     // construct a node with the middle element
     const node = new TreeNode(nums[mid]);

     // build left child
     node.left = helper(left, mid - 1);

     // build right child
     node.right = helper(mid + 1, right);

     // return the node
     return node;
   }
   
   return helper(0, nums.length - 1);
};


console.log(sortedArrayToBST([-10, -3, 0, 5, 9]));
console.log('');
console.log(sortedArrayToBST([]));



/**

     2
  3.    4
5. 6   6  7

  

/**
