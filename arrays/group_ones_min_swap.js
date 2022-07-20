// Group 0s and 1s

// Given an array of 0s and 1s, what is the minimum number of moves needed to group all 0s on one side and 1s on the other side. A "move" is a swap between any adjacent positions.

// Examples

// [0, 1] => 0, no swaps are needed since they are already grouped.
// [0, 1, 0] => 1, swap 1 with either 0 to group them.
// [1, 0, 1, 1, 0] => 2, swap 0 with 1 then swap it again with the next 1.

// [0,1,0,0,0] => 1

// [1, 1, 1, 1, 1, 0, 0, 1, 0]  
//.                      ^ 
//                 ^

// for loop 
//.   checks if element is 1, if yes
//      swapCount += pointer difference
//      increment slow pointer
//.     
// similarly, going from the other direction. 
// for loop first checks if it is 0 [..]

// return min of both swap counts.


// Function Signature

function minSwaps(array){
  let swapCount1 = 0
  let swapCount2 = 0
  let slowPointer = 0
  
  // loop
  for(let i=0; i<array.length; i++){
      if(array[i]==1){
        swapCount1 += i - slowPointer;

        slowPointer++;
      }
  }

  slowPointer = 0;

  for (let i = 0; i < array.length; i++) {
    if (array[i] === 0) {
      swapCount2 += i - slowPointer;

      slowPointer++;
    }

  }
  return Math.min(swapCount1, swapCount2);
}



const arr1 = [1,]
