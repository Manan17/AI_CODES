class Graph:
    def __init__(self,ad_list):
        self.ad_list = ad_list

    def heuristic(self,v):
        H = {
            'A':2,
            'B':1,
            'C':4,
            'D':0
        }
        return H[v]

    def get_neighbors(self,v):
        return self.ad_list[v]

    def a_star(self,start,destination):
        open_list=set([start])
        close_list=set([])
        distances={}
        adjacent_nodes={}
        distances[start] = 0
        adjacent_nodes[start] = start
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or distances[v] + self.heuristic(v) < distances[n] + self.heuristic(n):
                    n=v
            if n == None:
                print("Sorry Bhai")
                return 
            
            if n == destination:
                path=[]
                print("Path Midaala")
                while adjacent_nodes[n] !=n:
                    path.append(n)
                    n = adjacent_nodes[n]

                path.append(start)
                path.reverse()
                print(path)
                return
            
            for (neighbor,weight) in self.get_neighbors(n):
                if neighbor not in open_list and neighbor not in close_list:
                    open_list.add(neighbor)
                    distances[neighbor] = distances[n] + weight
                    adjacent_nodes[neighbor] = n
                else:
                    if distances[neighbor] > distances[n] + weight:
                        distances[neighbor] = distances[n] + weight
                        adjacent_nodes[neighbor] = n
                        if neighbor in close_list:
                            open_list.add(neighbor)
                            close_list.remove(neighbor)
            open_list.remove(n)
            close_list.add(n)
        print('Path does not exist!')
        return None 



graph = {
    'A':[('B',1),('C',1),('D',7)],
    'B':[('D',5)],
    'C': [('D', 2)]
}

g = Graph(graph)
g.a_star('A','D')

