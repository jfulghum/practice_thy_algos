/*
base case
recursive case
merge results - optional
*/

// 1->2->3 // 6
const sumAll = (head) => {
  if (!head) return 0

  return head.val + sumAll(head.next)
}

def sum_linked_list(head):
  if head is None:
    return 0
  return head.value + sum_linked_list(head.next)

  // n 
def recursiveSum(array, index=0):
  if len(array) == index:
    return 0 
  return array[index] + recursiveSum(array, index + 1)
  

// 1->2->3 

function getMax(head) {
  return max_element(head);  
}

function getMax(head) {
  max_element(head);
  return maxElement  
}


function getMax(head) {
  let max = head.data;
  max_element3(head, max);
  return max;
}

let maxElement = -Infinity;
function max_element1(head){

  if(!head){
    return maxElement;
  }
  if(head.data > maxElement){
    maxElement = head.data
  }

  return max_element(head.next);
}

function max_element2(head){

  if(!head){
   return;
  }
  if(head.data > maxElement){
    maxElement = head.data
  }

  max_element2(head.next);
}

function max_element3(head, max){

  if(!head){
   return;
  }

  if(head.data > max){
    max = head.data
  }

  max_element3(head.next, max);
}

1 
  2 
    3 

    3


    // 1 1 2 3 5 8 
def fib(n):
  if n < 2:
    return 1
  return fib(n - 1) + fib (n - 2)


      // 1 1 2 3 5 8 
def fib(n):
if n < 2:
  return 1
return fib(n - 1) + fib (n - 2) + fib(n-3)


def fib(n):
if n < 2:
  return 1
return fib(n/2) + fib((n-1)/2)

 2^(log(n))


1            1
3      2           3
7    4   5       6   7
15  8 9 10 11  12 13 14 15

[11]
[5]
[2]
[1]


2^n -1

            1
         2 3 4 5
        4k 4k 4k 4k

  // time 2 ^ n 
  // space linear 
