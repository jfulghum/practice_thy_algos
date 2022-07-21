# https://leetcode.com/problems/count-and-say/submissions/

class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'
        
        for _ in range(n - 1):
            new_string = ''
            curr_count, curr_num = 1, string[0]
            
            for i in range(1, len(string)):
                if string[i] == curr_num:
                    curr_count += 1
                else:
                    new_string += str(curr_count) + curr_num
                    curr_count, curr_num = 1, string[i]
            
            string = new_string + str(curr_count) + curr_num
            
        return string
      
print(countAndSay(4)) # 1211
