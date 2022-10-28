// # Given a linked list, determine if it has a cycle.
// # Function Signature: 

// # Target runtime and space complexity:
// # O(N)

// # Examples:
// # Input: 1 → 2 → 3
// # Output: False

// # Input:

// # 1 → 2 → 3  → 4 → 5 
// #         ↑________↓

// # Output: True

/*
      1 - 2 - 3 - 4
      ↑↓
  s   *
  f   *
  
      1 → 2 → 3 
      ↑________↓
  s                *
  f                *


      1 - 2 - 3 - 4 - null
                  ↑↓

  s           *
  f               *
  s, f both reach the end return false
  if fast ptr is equal to the slow ptr AND they are not at the end then return true 
*/


function has_cycle(head){
  if(!head){
    return false;
  }

  let slow = head;
  let fast = head;

  while (slow && slow.next && fast && fast.next){
    fast = fast.next.next;
    slow = slow.next;
    if(slow == fast){
      return true;
    }
  }

  return false;
}

class LLNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

// # 1 → 2 → 3  → 4 → 5 
// #         ↑________↓

let firstNode = new LLNode(1)
let secondNode = new LLNode(2);
let thirdNode = new LLNode(3);
let fourthNode = new LLNode(4);
let fifthNode = new LLNode(5);
firstNode.next = secondNode;
secondNode.next = thirdNode;
thirdNode.next = fourthNode;
fourthNode.next = fifthNode;
fifthNode.next = thirdNode;


const ll2 = new LLNode(5, new LLNode(6))

console.log(has_cycle(firstNode)) // True

console.log(has_cycle(ll2))// False
