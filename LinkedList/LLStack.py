# Prompt
# Implement a basic stack class using an linked list as the underlying storage. Stacks have two critical methods, push() and pop() to add and remove an item from the stack, respectively. You'll also need a constructor for your class, and for convenience, add a size() method that returns the current size of the stack. All of these methods should run in O(1) time!
# Remember, a stack is a first in, first out data structure!
# A singly linked list is a simple way to create a stack. The head of the list is the top of the stack.
# Function Signature

class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

class LLStack:
    def __init__(self):
      self.stack = []

    def size(self):
      return len(self.stack)

    def pop(self):
      return self.stack.pop()

    def push(self, item):
      return self.stack.append(item)

  
# Expected Runtime
# O(1) for all methods!
# Examples
stack = LLStack();
print(stack.size()) # 0
stack.push(2);
stack.push(3);
print(stack.size()) # 2
print(stack.pop()) # 3
print(stack.size()) # 1
print(stack.pop()) # 2
# Test various sequences of push/pop and be sure to test edge cases around an empty stack.
# Expected Questions
# If you were presented this question in an interview, these are some questions(s) you might want to ask:
# Q: Computing the size of a linked list is O(n). How can I make this constant?
# A: Keep track of the size as you push and pop in a separate field.
