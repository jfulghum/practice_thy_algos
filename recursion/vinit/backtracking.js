/*
Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point in time.

Given three students, who will refer to as “A”, “B”, and “C”, return an array representing all the combinations that they can sit in three seats. For example:

[ 'A', 'B', 'C' ]
[ 'A', 'C', 'B' ]
[ 'B', 'A', 'C' ]
[ 'B', 'C', 'A' ]
[ 'C', 'A', 'B' ]
[ 'C', 'B', 'A' ]

A sits in 1
  B sits in 2
    C sits in 3
  C sits in 2
    B sits in 3
B sits in 1
  A sits in 2
    C sits in 3
  C sits in 2
    A sits in 3
C sits in 1
  A sits in 2
    B sits in 3
  B sits in 2
    A sits in 3

- imagine you have a magic function that solves your use case for the N - 1 input
- figure out what you must do with the result of said magic function, to create the answer for the N input

getSeatArrangements([A, B, C])  // results: [[A, B, C], [A, C, B], [B, A, C], [B, C, A]]  i: 1

getSeatArrangements([A, B, C])
  getSeatArrangements([B, C])
    getSeatArrangements([C])
    getSeatArrangements([B])
  getSeatArrangements([A, C])
  ...
  getSeatArrangements([A, B])
  ...

[A] => [[A]]
[A, B] => [[A, B], [B, A]]
[A, B, C] => [
  [ 'A', 'B', 'C' ],
  [ 'A', 'C', 'B' ],
  [ 'B', 'A', 'C' ],
  [ 'B', 'C', 'A' ],
  [ 'C', 'A', 'B' ],
  [ 'C', 'B', 'A' ]
]

N * (N - 1) * (N - 2) ... 1
N!

*/

const getSeatArrangements = (students) => { // return list of lists
  if (students.length === 1) {
    return [students];
  }

  const results = []

  for (let i = 0; i < students.length; i++) {
    const studentInFirstSeat = students[i];
    const studentsExcludingKidInFirstSeat = [...students.slice(0, i), ...students.slice(i + 1)]
    const subArrangements = getSeatArrangements(studentsExcludingKidInFirstSeat)
    subArrangements.forEach(subArrangement => {
      results.push([studentInFirstSeat, ...subArrangement])
    })
  }

  return results;
}

console.log(getSeatArrangements(['A', 'B', 'C', 'D', 'E']))
