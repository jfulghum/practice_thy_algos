# https://www.dailycodingproblem.com/solution/128?token=30b19c5a8841788c9d5cc0dc9019e2a17dd0aa072619ab12dcb416109967e338b8a385bc

def tower_of_hanoi(n, a="1", b="2", c="3"):
    if n >= 1:
        tower_of_hanoi(n - 1, a, c, b)
        print("Move {} to {}".format(a, c))
        tower_of_hanoi(n - 1, b, a, c)
        
# If there is more than 1 disk, then we can do the following:           
# Recursively move n - 1 disks from the source stack to the spare stack (A to B)
# Move the last (biggest) disk from the source stack to the target stack (A to C)
# Recursively move all n - 1 disks from the spare stack to the target stack (B to C)   
        
        
# This will run in O(2n) time, since for each call we're recursively calling ourselves twice. 
# This should also take O(n) space since the function call stack goes n calls deep.
