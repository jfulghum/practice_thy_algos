/*

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.

Example:

Given the list of temperatures T = [73, 74, 75, 71, 69, 72], your output should be [1, 1, 0, 2, 1, 0]

Approach 1:
- Two for loops
Time complexity: O(n^2)

[73, 74, 75, 71, 69, 72]/*

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.

Example:

Given the list of temperatures T = [73, 74, 75, 71, 69, 72], your output should be [1, 1, 0, 2, 1, 0]

Approach 1:
- Two for loops
Time complexity: O(n^2)

Approach 2:

Time complexity: O(n)

*/

function dailyTemps(T){
  let i = 0;
  const result = [];

  while (i < T.length) {
    let j = i + 1;
    while (j < T.length) {
      if (T[j] > T[i]){
        result.push(j - i);
        break;
      }
      j++
    }
    if (j === T.length) {
      result.push(0);
    }
    i++;
  } 

  return result;
}

/*

[73, 74, 75, 71, 69, 72]

stack [2, 3]
result [1, 1, 0, 2, 1, 0]

i = 5
cur = 72



*/

const dailyTemps2 = (T) => {
  const stack = [];
  const result = new Array(T.length).fill(0);
  
  for (let i = 0; i < T.length; i++) {
    const cur = T[i];

    while (stack.length !== 0 && T[stack[stack.length - 1]] < cur) { // cur is larger than temp at top of stack
      result[stack[stack.length - 1]] = i - stack[stack.length - 1];
      stack.pop();
    }
    
    stack.push(i); // push every index we've seen into stack at end of loop
  }

  return result;
}



// Test Cases
console.log(dailyTemps2([60]), '[0]');
console.log(dailyTemps2([73, 73]), '[0, 0]');
console.log(dailyTemps2([73, 73, 62]), '[0, 0, 0]');
console.log(dailyTemps2([73, 74, 75, 71, 69, 72]), '[1, 1, 0, 2, 1, 0]');

result [1]
i = 0

  current = 73
  count 1
  j = 1


*/

function dailyTemps(T){
  let i = 0;
  const result = [];

  while (i < T.length) {
    let j = i + 1;
    while (j < T.length) {
      if (T[j] > T[i]){
        result.push(j - i);
        break;
      }
      j++
    }
    if (j === T.length) {
      result.push(0);
    }
    i++;
  } 
  
  return result;
}

// Test Cases
console.log(dailyTemps([60]), '0');
console.log(dailyTemps([73, 73]), '[0, 0]');
console.log(dailyTemps([73, 73, 62]), '[0, 0, 0]');
console.log(dailyTemps([73, 74, 75, 71, 69, 72]), '[1, 1, 0, 2, 1, 0]');
