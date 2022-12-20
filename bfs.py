graph = {
5 : [3, 7],
3 : [2, 9, 4],
7 : [8],
2 : [],
4 : [2],
8 : []
}
openlist=[]
closelist=[]
path=[]
start=5

def bfs(graph1,open,close,start_node,goal_node):
    open.append(start_node)
    while open:
        extracted_node = open.pop(0)
        close.append(extracted_node)
        path.append(extracted_node)
        if extracted_node == goal_node:
            print(f'Path is {path}')
            return 
        for neighbour in graph1[extracted_node]:
            if neighbour not in graph1.keys():
                print("Not in graph is ",neighbour)
                continue
            if neighbour not in close:
                open.append(neighbour)

    return "Goal not found"

bfs(graph,openlist,closelist,start,2)
                