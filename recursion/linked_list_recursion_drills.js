/*
Problem List  - Recursion on Linked Lists

You don't have to get through all of these in the session. Instead, strive for an optimal learning experience.
Use recursion to write code for the following problems:


1. - Given a linked list and an integer, find whether the integer exists in the list. Return a boolean. -Cal
2. - Given a linked list and an integer, return how many times the integer exists in the list. -Alec
- Find mean of a list of integers - Alec
- Replace all negative values with a 0
- Reverse the list - cal


*/


function listToStr(head) {
  const parts = [];
  while (head) {
    parts.push(head.value);
    head = head.next;
  }
  return "{" + parts.join(" -> ") + "}";
}

class Node{
   constructor(value, next = null){
    this.value = value;
    this.next = next;
   }
}
//------------------------------------------------------------------

const search = (head, num) => {
    let curr = head;
    if(!curr){
      return false
    }
    if(curr.value === num){
      return true;
    }
    return search(curr.next, num);
}

let LL = new Node(1, new Node(2, new Node(3, new Node(2))));
// console.log(search(LL, 3));

// search(curr.next, num)


/* 
2. - Given a linked list and an integer, return how many times the integer exists in the list. -Alec
*/

// 1 => 2 => 3 => target is 2 => 1
// function numExists(head, target){
//   if(!head) return 0;
//   if(head.value === target){
//     return 1 + numExists(head.next, target)
//   }
//   return numExists(head.next, target);
// }

function numExists(head, target){
  if(!head) return 0;
  
  return +(head.value === target) + numExists(head.next, target)
 
}

// console.log(numExists(LL, 2)); //2


// Find mean of a list of integers

//  mean = sum / count 

/*
  1=>2=>3=>2

  return curr.value + sum(curr.next))

*/

function mean(head){
  if(!head) return 0;
  // let total = 0
  // let count = 0 
  function sumAndCount(head){
    if(!head) return [0, 0];


    const [sum, count] = sumAndCount(head.next)

    return [head.value + sum, count+1]
    
  }
  const [sum, count] = sumAndCount(head)

  return sum / count

}


console.log(mean(LL)) 
// 2



function reverse(head) {
  if (!head || !head.next) {
    return head;
  }
  let tmp = reverse(head.next);
  head.next.next = head;
  head.next = undefined;
  return tmp;
}

console.log(listToStr(reverse(LL)))
