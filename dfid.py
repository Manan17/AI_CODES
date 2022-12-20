graph = {
5 : [3, 7],
3 : [2, 4],
7 : [8],
2 : [],
4 : [8],
8 : []
}

def DFS(currentNode,goalNode,graph,maxDepth):
    print(currentNode)
    if currentNode == goalNode:
        return True
    if maxDepth <=0:
        return False
    
    for node in graph[currentNode]:
        if DFS(node,goalNode,graph,maxDepth-1):
            return True

    return False

def IDDFS(currentNode,goalNode,graph,maxDepth):
    for i in range(maxDepth):
        if DFS(currentNode,goalNode,graph,i):
            return True

    return False

print(IDDFS(5,8,graph,3))