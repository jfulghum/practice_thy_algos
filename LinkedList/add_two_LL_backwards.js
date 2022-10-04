

// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example 1:
// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.

//         342
//         465
//         ___
          


// Example 2:
// Input: l1 = [0], l2 = [0]
// Output: [0]
// Example 3:

// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

// Q: if numbers are NOT reversed (in correct order), should we still reverse the order to start summing least significant digits?
// We need to reverse the LL to emulate how large digit division is done by hand on paper (starting with ones place)

// instantiate result list, dummy head should suffice
// instantiate "carry" var to 0

// loop through both linked lists simultaneously
//   - add curNode value of both lists AND carry
//   - mod by 10 will give us the value we want to create a new node with (create node and append to our result list)
//   - divide by 10 floored will give us the carry digit

// return dummy head.next

// */

class LLNode {
  constructor(val, next = null) {
    this.val = val;
    this.next = next;
  }
}

/*

342 + 65 => 407

head1: 2 => 4 => 3 => null
cur1:                 ^

head2: 5 => 6 => null
cur2:            ^

dummyHead: 0 => 7 => 0 => 4 => null
resultCur:                ^

carry: 0

summedNum: 10


*/

const ll1 = new LLNode(2, new LLNode(4, new LLNode(9)))
const ll2 = new LLNode(5, new LLNode(6))

const sumLinkedLists = (head1, head2) => {
  const dummyHead = new LLNode(0);
  let resultCur = dummyHead;
  let carry = 0;
  let cur1 = head1;
  let cur2 = head2;

  while(cur1 || cur2) {
    const summedNum = (cur1 ? cur1.val : 0) + (cur2 ? cur2.val : 0) + carry;
    resultCur.next = new LLNode(summedNum % 10);
    resultCur = resultCur.next;
    carry = Math.floor(summedNum / 10);
    if (cur1) {
      cur1 = cur1.next; 
    }
    if (cur2) {
      cur2 = cur2.next; 
    }
  }

  if (carry !== 0) {
    resultCur.next = new LLNode(carry);
  }

  return dummyHead.next;
}

console.log(sumLinkedLists(ll1, ll2)) // list with 7, 0, 4
