/*

Given an m x n matrix, return all elements of the matrix in spiral order.

const test1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

const test2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
];

rowStart = 0
rowEnd = matrix.length - 1
colStart = 0
colEnd = matrix[0].length - 1

- 1st loop (left to right at top)
  - go through current rowStart from colStart to colEnd
- increment rowStart by 1

- 2nd loop (top to bottom on right)
  - go through current colEnd from rowStart to rowEnd
- decrement colEnd by 1

- 3rd loop (right to left at bottom)
  - go through current rowEnd from colEnd to colStart
- decrement rowEnd by 1

- 4th loop (bottom to top on left)
  - go through current colStart from rowEnd to rowStart
- increment colStart by 1

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

*/

const test1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

const test2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
];

const returnInSpiralOrder = (matrix) => {
  const result = [];
  let rowStart = 0;
  let rowEnd = matrix.length - 1;
  let colStart = 0;
  let colEnd = matrix[0].length - 1;

  while (rowStart <= rowEnd && colStart <= colEnd) {
    for (let i = colStart; i <= colEnd; i++) {
      result.push(matrix[rowStart][i])
    }
    rowStart++;
    
    for (let i = rowStart; i <= rowEnd; i++) {
      result.push(matrix[i][colEnd])
    }
    colEnd--;

    if (rowStart <= rowEnd) {
      for (let i = colEnd; i >= colStart; i--) {
        result.push(matrix[rowEnd][i]);
      }
    }
    rowEnd--;
    
    if (colStart <= colEnd) {
      for (let i = rowEnd; i >= rowStart; i--) {
        result.push(matrix[i][colStart]);
      }
    }
    colStart++;
  }
  
  return result;
}

// console.log(returnInSpiralOrder(test1)); // [1,2,3,6,9,8,7,4,5]
console.log(returnInSpiralOrder(test2)); // [1,2,3,4,8,12,11,10,9,5,6,7]
