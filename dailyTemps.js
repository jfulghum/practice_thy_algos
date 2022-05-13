/*

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.

Example:

Given the list of temperatures T = [73, 74, 75, 71, 69, 72], your output should be [1, 1, 0, 2, 1, 0]

Approach 1:
- Two for loops
Time complexity: O(n^2)

[73, 74, 75, 71, 69, 72]

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
