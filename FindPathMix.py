def find_path(graph, start, end, path=[]):
    path = path + [start]
#    print(path)
    if start not in graph: #when start node is wrong
       return None
    if start == end:
        return path
    #if not graph.has_key(start):
     #   return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start not in graph:
            return None
        if start == end:
            return [path]

        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start not in graph:
            return  None
        if start == end:
            return path

        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

print(find_path(graph,'A','B'))
print(find_all_paths(graph,"A","C"))
print(find_shortest_path(graph,"A","D"))