def toAdjList(vertexList, edgeList):
    output = {}
    for v in vertexList:
        output[v] = []
    for v1, v2 in edgeList:
        output[v1].append(v2)
        output[v2].append(v1)
    return output

def sumNodes(vertexList: list, edgeList: list, startNode: int) -> int:
    if startNode not in vertexList:
        return 0

    adj_list = toAdjList(vertexList, edgeList)
    visited = set()
    total = 0
    def dfs(curr):
        nonlocal total
        if curr in visited:
            return
        total += curr
        visited.add(curr)
        for neighbor in adj_list[curr]:
            dfs(neighbor)
    dfs(startNode)
    return total
