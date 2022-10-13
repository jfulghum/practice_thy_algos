
/*
Given a matrix of size N by M, find the number of unique paths from the top left cell to the top right cell. The only valid moves that can be made are:
- 1 step to the right
- 1 step diagonally up and to the right
- 1 step diagonally down and to the right

[+, 0, +]
[0, 0, 0]
[0, 0, 0]

[1, 1, 1]
[0, 0, 0]
[0, 0, 0]

[1, 0, 1]
[0, 1, 0]
[0, 0, 0]

[+, 0, 0, +]
[0, 0, 0, 0]
[0, 0, 0, 0]

[1, 1, 1, 1]
[0, 0, 0, 0]
[0, 0, 0, 0]

[1, 0, 1, 1]
[0, 1, 0, 0]
[0, 0, 0, 0]

[1, 1, 0, 1]
[0, 0, 1, 0]
[0, 0, 0, 0]

[1, 0, 0, 1]
[0, 1, 1, 0]
[0, 0, 0, 0]

from the starting point: how many choices do i have

                                                      (0,0)
                      (-1,1)                          (0,1)                                  (1,1)
                                   (-1,2)             (0,2)       (1,2)             (0,2)    (1,2)      (2,2)

O(3^(NM))

*/

const numPaths = (matrix, x = 0, y = 0) => {  // return number
  if (x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length) {
    return 0;
  }
  if (x === 0 && y === matrix[0].length - 1) {
    return 1;
  }

  return numPaths(matrix, x - 1, y + 1) + numPaths(matrix, x, y + 1) + numPaths(matrix, x + 1, y + 1)
}

const testMatrix1 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

const testMatrix2 = [
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]

console.log(numPaths(testMatrix1))
console.log(numPaths(testMatrix2))
