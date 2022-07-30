/*

A Toeplitz matrix is one where all elements along diagonals from top left to bottom right are the same. Given a matrix, return true if it is a Toeplitz matrix and false otherwise.

Example:

This is a Toeplitz matrix:

loop through the first row, 
for every item, look 1 index over and one down and compare until out of bounds if false, return false. 
loop through the first col, (skip first one)
for every item, look 1 index over and one down and compare until out of bounds. if false, return false. 

1  2  3  4
5  1  2  3
6  5  1  2
7  6  5  1

This is not a Toeplitz matrix:

1  2
2  2


1 0 1
0 1 0
1 0 1

1
*/

// Lesson is don't overcomplicate

function isToeplitz(mat) {
  if (mat.length !== mat[0].length) return false
  
  for (let row = 0; row < mat.length - 1; row++) {
    for (let col = 0; col < mat[0].length - 1; col++) {
      if (mat[row + 1][col + 1] !== mat[row][col]) return false
    }
  }

  return true
}

const mat1 = [
  [1, 2, 3, 4],
  [5, 1, 2, 3],
  [6, 5, 1, 2],
  [7, 6, 5, 1]
]
console.log(isToeplitz(mat1), true)

const mat2 = [[1, 2], [2, 2]]
console.log(isToeplitz(mat2), false)

// console.log(isToeplitz([]), true)

const m3 = [
[1, 0, 1],
[0, 1, 0],
[1, 0, 1]]

console.log(isToeplitz(m3),true)

const mZ = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]]

console.log(isToeplitz(mZ),true)

console.log(isToeplitz([[1,2],
                        [3,1]]), true)
            
console.log(isToeplitz([[1,4],
                        [3,8]]), false)




function isToeplitz(matrix) {
  
  for (let i = 0; i < matrix.length; i++) {
    let iAlt = matrix.length - 1 - i;

    for(let j = 0; j < matrix.length; j++) {
      let jAlt = matrix.length - 1 - j;

      if (matrix[i][j] !== matrix[jAlt][iAlt]) {
        return false;    
      }

      if(jAlt === j) {
        break   
      }   
  
    }
  }
  return true;
}


let test1 = [[1, 2, 3, 4],[5, 1, 2, 3],[6, 5, 1, 2],[7, 6, 5, 1]];
let test2 = [[1,2],[2,2]];
console.log(isToeplitz(test1));
console.log(isToeplitz(test2))
