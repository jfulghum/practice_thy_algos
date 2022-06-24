/*
The programming interface for a legacy motor controller accepts commands as binary strings of variable length. The console has a very primitive autocomplete autocorrect feature: given an incomplete command, it will display possible commands that has the incomplete command as a prefix. For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result.
Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.
Example
Possible commands = ['000', '1110', '01', '001', '110', '11']
Input -> Output
'0' → ['000', '01', '001']
'1' → ['1110', '110', '11']
'00' → ['000', '001']
'' -> []
'1110' -> ['1110']
'11'-> ['1110', '11', '110']

Approach 1:
Time Complexity: ??
* Building a trie
   - Insert string into a trie, O(k * n) length of input string given * (n) number of elements in array, k = avg len of char in array
   - navigate in a trie - return every string that has terminating character (*), depth is bounded by the height, and bounded by the longest string  O(s + 2^k-s); s = len of string, k = len of longest string 
Trie - prefix tree
TrieNode
- value - char
- listOfchildren - {} collection TrieNodes
- endOfString - boolean (*)

                root
               0       1
              / \       \
              0  1(*)    1(*)
            /  \        / \
          0(*)  1(*)  0(*) 1
                            \
                             0(*)

** Useful only if you had a list of strings to input into the trie, and if you had to do multiple lookup and it would be more efficient to navigate 
                           
Approach 2:
Time complexity: O(s * n ) - (s) length of input string given * (n) number of elements in array
Space Complexity: O(c) c = len of commands array
- Brute force solution? - avoid using it
- Filter an array for the input

autocomplete(input: String) → List[String]

find the length input 
loop through the possible commands 
if they match return in a new array 
*/



function autocomplete(input, commands) {
  if(!input.length) return [];

  const res = commands.filter((value)=>{
    return value.startsWith(input)
  })

  return res;
}

function autocomp(input, commands) {
  return !input.length ? [] : commands.filter((value)=>{
    return value.startsWith(input)
  })
}

// Test Cases
const commands = ['000', '1110', '01', '001', '110', '11'];
console.log(autocomplete('001', commands));
console.log(autocomplete('0', commands));
console.log(autocomplete('', commands));
console.log(autocomplete('1110', commands), "['1110']")
console.log(autocomplete('11', commands), "=> ['1110', '11', '110']")
