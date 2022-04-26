def returnAllSubsequences(input, output):
    if len(input) == 0:
        return [output]
    results = []
    results.extend(returnAllSubsequences(input[1:], output+input[0]))
    results.extend(returnAllSubsequences(input[1:], output))
    return results

     
print(returnAllSubsequences(input="abcd", output=""))
