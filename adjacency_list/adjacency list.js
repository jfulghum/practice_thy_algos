/*
Given an adjacency list of a directed graph, return "BINARY TREE" if it's a binary tree, "TREE" if it's any other type of tree, or "NONE" if it's neither.
Examples
     1
   /   \ 
 2     3
/
4

# no more than 2 element in value array
# each key has excatly 1 parent (in a value array) (excluding 1)

# 

{
  1: [2],
  2: [1]
} => NONE


input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: []
    }
) -> BINARY TREE
--------------

     1        5
   /   \ 
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
        5: [],
    }
) -> NONE

--------------

     1       
   /   \ 
 2      3
   \   /
     4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [],
    }
) -> NONE
Function Signature
classify(adj_list)


    {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [],
    }

visited_nodes = [1,2]

queue = [3, 4]


{
  1: [2],
  2: [3],
  3: [1]
}

visited_nodes = [1,2,3]
queue = [1]



     1        5
   /   \ 
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
        5: [],
    }
) -> NONE




visited_nodes = [1,2,3,4]
queue = []
NONE since len(visited_nodes) != len(input)




     1
   /   \ 
 2     3
/
4

classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: []


to find the root

get the keys and the values and compare the two
whatever key is not in values would be a potential root
  if we have more than one root, return none

  create keys set 
  root = None
  for value in values:
      if key in values:
        remove key from set
  
  if length of set is not 1, return 'NONE'

  then move on to plan underneath


Plan:
Create a queue
Create visited set
Set result to 'BINARY TREE'

While queue is not empty
    Shift out the first element of the queue and add its adjacencies to the queue
    If the shifted element is in the visited set, return NONE
    If the length of the adjacencies is greater than 2, set result to 'TREE'
    
check that the visited set has an equal length to the input. if it's not return 'NONE'
return result    

*/

function classify(adjacencyList) {
  const keySet = new Set(Object.keys(adjacencyList));
  const values = Object.values(adjacencyList).flat();
  let root;

  for (let value of values) {
    value = value.toString()
    keySet.delete(value)
  }

  console.log('key set', keySet);
  if (keySet.size != 1){
    return 'NONE'
  }
  root = keySet[0]
  
  const queue = [root];
  const visited = new Set();
  let result = 'BINARY TREE';

  while (queue.length) {
    const node = queue.shift();
    
    if (visited.has(node)) return 'NONE';

    if (adjacencyList[node].length > 2) {
      result = 'TREE'
    }

    queue.concat(adjacencyList[node.toString()]);
  }

  if (visited.length !== Object.keys(adjacencyList).length) return 'NONE';
  return result;
}

console.log(classify(
  {
      1: [2, 3],
      2: [4],
      3: [],
      4: []
  }
), 'BINARY TREE')

// console.log(classify
//   {
//       1: [2, 3],
//       2: [4],
//       3: [],
//       4: [],
//       5: [],
//   }
// ), 'NONE')

// console.log(classify(
//   {
//       1: [2, 3, 5],
//       2: [4],
//       3: [],
//       4: [],
//       5: []
//   }
// ), 'TREE');

// console.log(classify(
//   {
//       1: [2],
//       2: [1],
//   }
// ), 'NONE');
