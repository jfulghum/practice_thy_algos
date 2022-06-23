/*
The programming interface for a legacy motor controller accepts commands as binary strings of variable length. The console has a very primitive autocomplete autocorrect feature: given an incomplete command, it will display possible commands that has the incomplete command as a prefix. For example, if '1010' is a possible command and the user enters '10', the interface should return '1010' as a possible autocomplete result.
Implement a data structure that will allow us to efficiently query possible autocomplete results given an incomplete input.
Examples
Possible commands = ['000', '1110', '01', '001', '110', '11']
Input -> Output
'0' → ['000', '01', '001']
'1' → ['1110', '110', '11']
'00' → ['000', '001']
'' -> []
'1110' -> ['1110']
'11'-> ['1110', '11', '110']

Approach 1:
Trie - prefix tree
TrieNode
- value - char
- listOfchildren - {} collection TrieNodes
- endOfString - boolean (*)

                root
              0        1
              / \       \
              0  1(*)    1(*)
              / \       / \
          0(*)  1(*)    0  1(*)
                          \
                           0(*)

                           
Approach 2:
Time complexity:
Brute force solution?
- Filter an array for the input

autocomplete(input: String) → List[String]
*/
