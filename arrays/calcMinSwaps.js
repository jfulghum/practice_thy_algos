/*

Given an array of 0s and 1s, what is the minimum number of moves needed to group all 0s on one side and 1s on the other side. A "move" is a swap between any adjacent positions.

Examples:

[0, 1] => 0, no swaps are needed since they are already grouped.
[0, 1, 0] => 1, swap 1 with either 0 to group them.
[1, 0, 1, 1, 0] => 2, swap 0 with 1 then swap it again with the next 1
[1, 1, 0, 1, 0]
[1, 1, 1, 0, 0]

[1, 0, 1, 1, 0]
    l        r
    
google meet kicked me out lol
do you want us to send you the link again?
can ya'll try to join this https://meet.google.com/fae-jkoc-sos

Notes:
-len(input) <= 2, ret 0

Pseudocode(2 Bubble-Sorts):
1) Instantiate numSwaps = 0
2) Perform Bubble Sort
Outer loop:
  Inner loop starting 1 pointer ahead of where the outer loop is starting:
    Compare elements at outer loop pointer and inner loop pointers
      If inner loop element > outer loop element, swap and increment numSwaps
    Move outer pointer and inner pointer forward(so pointers are adjacent)

3) Repeat Bubble Sort, but this time flip swap condition
4) Return lowest numSwaps
      
      
1 0 0 0 0  - 4 steps to get the 1 to the right
1 1 0 0 0 0 - 8 steps to get both 1s to the right
1 1 1 0 0 0 0 - 12 steps to get all 1s to the right

number of 1s times number of 0s they need to move through === num steps

1 0 0 1 1 0 0 1 0
^ 2 steps
0 0 1 1 1 0 0 1 0
    ^ 6 steps
0 0 0 0 1 1 1 1 0
        ^ 4 steps
0 0 0 0 0 1 1 1 1

numberOf1s * steps
numberOf1s + numberOf1s + numberOf1s ... steps times


1 0 1 0 0 1 0
            ^

numOnes: 3
totalMoves: 8

minSwaps(input) N
minSwaps(input.reverse()) N + N

*/

const solution = binArray => {
  const calcMinSwaps = binArray => {
    let numOnes = 0;
    let totalMoves = 0;
    for (let i = 0; i < binArray.length; i++) {
      binArray[i] === 1 ? numOnes++ : totalMoves += numOnes;
    }
    return totalMoves;
  }

  return Math.min(calcMinSwaps(binArray), calcMinSwaps(binArray.reverse()));
}


console.log(solution([1,0, 0, 1, 1, 0, 0, 1, 0]), "12")
console.log(solution([1,0, 1, 0, 0, 1, 0]), "8")
