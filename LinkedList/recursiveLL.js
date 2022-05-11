/**
Use RECURSION to write code for the following problems:

Given a linked list and an integer, find whether the integer exists in the linked list. Return a boolean.

- define the function
-create a helper function 
  -base case: check if weve reached end of the linked list, if so, return false;
  -check if the value matches what we are lookign for, if so return true;
  -recurse
-call the helper func

count nodes
  node   node  ->  node -> null -> 
  1+2     1+1      1 + 0       0

Given a linked list and an integer, return how many times the integer exists in the list.
  - if node is null, return 0
  - count = 0
  - check if value equals integer
    -- increment count
  -return count + func(next node), 
*/
class ListNode {
  constructor(val = 0, next = null) {
    this.value = val;
    this.next = next;
  }
}


function count(node, target){
  if (node === null) {
    return 0
  }
  
  // return ((node.value === target).length() + count(node.next, target)
  return (node.value === target ? 1: 0) + count(node.next, target)
}



// console.log(count(null, 1), 0)
// console.log(count(node1, 9), 1)
// console.log(count(node2, 17), 0)
// console.log(count(node2, 2), 2)



/*
****Find average of a list of integers
*/

function average(node){
  if(!node) return 0;
  let length = 0;
  let sum = 0;

  function helper(node):void{
    if(!node) return;
    sum += node.value;
    length++;

    return helper(node.next);
  }

  return sum / length;
}
let node1 = new ListNode(9)
let node2 = new ListNode(1, new ListNode(2, new ListNode(5, new ListNode(2, null))));

// console.log(average(node2), 2.5) // 2.5
console.log(average(null), 0)
// console.log(average(node1), 9)

/*

Replace all negative values with a 0


Reverse the list 

# prev, curr = None, head
nextNode = prev
curr.next = nextNode



     <- 1<-2    3 -> 4  
                t
null 
           p     
                rf



prev = null

recursive function:
  base case

  temp = node.next
  node.next = prev
  prev = node
  recursive(temp)
--
return prev

 */

function exists(head, k) {
    const helper = (node, k) => {
        if (!node) {
            return false
        }

        if (node.value === k) {
            return true
        }

        return helper(node.next, k)
    }

    return helper(head, k)
}





let node = new ListNode(9)
// console.log(exists(node, 9)) // True

// let test1 = new ListNode(1, new ListNode(2, new ListNode(5, new ListNode(9, null))));

// console.log(exists(null, 1), false)
// console.log(exists(node, 9), true)
// console.log(exists(test1, 9), true)
// console.log(exists(test1, 10), false)
