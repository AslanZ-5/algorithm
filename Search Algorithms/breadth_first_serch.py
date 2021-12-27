testgraph = {'0': ['3', '5', '9'],
             '1': ['6', '7', '4'],
             '2': ['10', '5', ],
             '3': ['0'],
             '4': ['1', '5', '8'],
             '5': ['2', '0', '4'],
             '6': ['1'],
             '7': ['1'],
             '8': ['4'],
             '9': ['0'],
             '10': ['2']

             }


def dfs(graph, startNode):
    visitedNodes = []
    queue = [startNode]

    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)
    return visitedNodes


