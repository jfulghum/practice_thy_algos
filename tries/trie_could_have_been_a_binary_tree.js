/**
 * 
 The programming interface for a legacy motor controller accepts commands as binary strings of variable length. The console has a very primitive autocomplete autocorrect feature: given an incomplete command, it will display possible commands that has the incomplete command as a prefix. For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result.


Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.

Examples

Possible commands = ['000', '1110', '01', '001', '110', '11']

Input -> Output

'0' → ['000', '01', '001']
'1' → ['1110', '110', '11']
'00' → ['000', '001']


// Possible approach 1
O(n) where n is the number of element in array * O(m) where m is length of input string
// take the input, and loop through the array, if the element starts with the input,
// appened to finalArray
// return the finalArray
/
// Possible approach 2 Trie

**/

// key, maps, bool enOfWord

class TrieNode {
  constructor(key){
    this.key = key;
    this.children = {};
    this.endOfWord = false;
  }
}

//Trie insert

class Trie {
  constructor(){
    this.root = new TrieNode(null)
  }

  insert(word){
    let current = this.root
    for(char of word){
      if(current.children[char] === undefined){
        current.children[char] = new TrieNode(char)
      }
      current = current.children[char]
    }
    current.endOfWord = true;
  }

  /*
    children: {
      "0": new TrieNode(...),
      "1": new TrieNode(...),
    }


    '0' → ['000', '01', '001']
    Conditions?
    1. endOfWord == true


         null
         0      1
      0     1
    0   1 
  */
  search(input) {
    let charactersSeenSoFar = input;
    let result = [];
    let curr = this.root
    for (char of input) {
      if (curr.children[char]) {
        curr = curr.children[char];
        
      }
    }
    
    if(Object.keys.size(curr.children) > 0){
      for(key of curr.chidlren){
        charactersSeenSoFar += key;
        if(curr.children[key].endOfWord === true){
          result.push(charactersSeenSoFar)
        }
      }
    }

    
    if(endOfWord) {

    }
  }

}

  // loop though each char of the input number
  // if match, go to the bottom of each branch of that tree, and return those numbers 
//   input = 10 
// return 101, 102

//     1

//   0

// 1*   2*




