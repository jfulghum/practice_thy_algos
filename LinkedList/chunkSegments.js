// Given the head node of a linked list and any number (k), break your list into (k) consecutive chunks, with no two chunks should have a size differing more than one.
// The result chunks should be in the same original order, and chunks occurring earlier should never be smaller than later chunks.
// Return an array of all (k) chunks.
// Function Signature: 
// Example 1

// 1 -> 2 -> 3 -> 4 -> 5, k = 5 should return [[1], [2], [3], [4], [5]]
// Example 2

// 1 -> 2 -> 3, k = 5 should return [[1], [2], [3], [], []]
// Example 3

// 2 -> 2 -> 3 -> 4 -> 5 -> 6 -> 4 -> 8 -> 9 -> 10, 
// k = 3 should return [[2,2,3,4],[5,6,4],[8,9,10]]

class ListNode {
  constructor(value = null, next = null) {
    this.value = value;
    this.next = next;
  }
}

function chunkSegments(head, n){

  if (n < 1) return null;

  function getLength(head) {
    let curr = head;
    let count = 0;
    while (curr) {
      count++;
      curr = curr.next;
    }
    return count;
  }

  const length = getLength(head);
  const minNodes = Math.floor(length/n);
  let leftoverNodes = length % n;

  let curr = head;
  const chunks = [];

  for (let i = 0; i < n; i++) {
    const chunk = [];
    for (let j = 0; j < minNodes; j++) {
      if (curr) {
        chunk.push(curr.value);
        curr = curr.next;
      }
    }
    if (leftoverNodes > 0) {
      chunk.push(curr.value);
      curr = curr.next;
      leftoverNodes--;
    }
    chunks.push(chunk);
  }
  return chunks;
}

// n loops * minNodes -> length/n

// 1 -> 2 -> 3 -> 4 -> 5, k = 5 should return [[1], [2], [3], [4], [5]]
const list1 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
const list2 = new ListNode(1, new ListNode(2, new ListNode(3)))
console.log(chunkSegments(list1, 5), [[1], [2], [3], [4], [5]]);
console.log(chunkSegments(list2, 5), [[1], [2], [3], [], []])
console.log(chunkSegments(list1, 0), null);
console.log(chunkSegments(null, 1), [[]]);
console.log(chunkSegments(list1, 2), [[1, 2, 3], [4, 5]])

// if k is less than 1, return null
// if k is one, return an array of the values
// if list is empty, return k empty arrays

// determine length of list
// minNodes -> floor of list length / k -> general # of nodes for each array
// modulo of list % k -> leftover nodes

// declare empty result array
// curr pointer starting at list head

// k loops
  // if curr is ever null, break out of iteration but still push new array 
  // iterate forward by minNodes nodes -> push value to a new array
  // if there are leftovers, iterate one more and decrement leftover count
  // push new array to result array

// return result array

// #heather
