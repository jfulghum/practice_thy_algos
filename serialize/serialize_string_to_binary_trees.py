class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        
        if not s:
            return None
        
        root = TreeNode()
        stack = [root]
        
        index = 0
        while index < len(s):
            
            node = stack.pop()

            # NOT_STARTED
            if s[index].isdigit() or s[index] == '-':
                value, index = self._getNumber(s, index)
                node.val = value

                # Next, if there is any data left, we check for the first subtree
                # which according to the problem statement will always be the left child.
                if index < len(s) and s[index] == '(':
                    stack.append(node)

                    node.left = TreeNode()
                    stack.append(node.left)
            
            # LEFT_DONE
            elif node.left and s[index] == '(':
                stack.append(node)

                node.right = TreeNode()
                stack.append(node.right)
            
            index += 1
        return stack.pop() if stack else root
    
    def _getNumber(self, s: str, index: int) -> (int, int):
        
        is_negative = False
        
        # A negative number
        if s[index] == '-':
            is_negative = True
            index = index + 1
        
        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        return number if not is_negative else -number, index
      
      
      
# Input: s = "4(2(3)(1))(6(5))"
# Output: [4,2,6,3,1,5]
# Example 2:

# Input: s = "4(2(3)(1))(6(5)(7))"
# Output: [4,2,6,3,1,5,7]
# Example 3:

# Input: s = "-4(2(3)(1))(6(5)(7))"
# Output: [-4,2,6,3,1,5,7]
