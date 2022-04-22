'''
Prompt:
Given an input dictionary mapping Fellows (as string names) to skill ratings, return true if you're able to pair up Fellows with matching skill ratings with no Fellows leftover.

Function Signature:
function canMatchFellows(input)

Examples
{"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5} => true
{"oliver": 3, "pixel": 4, "pinky": 5, "tobey": 5} => false
{} => false


{"Jorie":1, "Johanna":2, "Juliette":3, "Kendallene":1, "David":2, "Keith";3} => true
'''

#Identify Simple Solution (Brute Force is Okay)
# set()

# {"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5}
# ^ 
# loop through and add value to set if there, remove if not, at the end return if len of set


def canMatchFellows(ratingbyFellow):
    result = set()
    for _, value in ratingbyFellow.items():
        if value in result:
            result.remove(value)
        else:
            result.add(value)
    return not result


print(canMatchFellows({"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5})) # true
print(canMatchFellows({"oliver": 3, "pixel": 3, "pinky": 4, "tobey": 5})) # false
print(canMatchFellows({"oliver": 3, "pixel": 3, "pinky": 5, "tobey": 5, 'Johanna': 4})) # false

