n = int(input())
graph = dict()

v1 = 0
for i in range(n):
    v1, v2 = list(map(int, input().split()))
    if v1 not in graph:
        graph[v1] = []
    if v2 not in graph:
        graph[v2] = []
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)

____________________________

using iterative version of dfs where u push the node from stack , its children then its children till all are exhausted
stack = [1]
seen = set()
vis_ord = []
while len(stack) != 0:
    fr = stack.pop()
    if fr not in vis_ord:
        vis_ord.append(fr)
    for node in graph[fr]:
        if node not in seen:
            seen.add(node)
            stack.append(node)
        
print(vis_ord)

__________________________________
using bfs with an adjacency list, on an undirected, unweighted graph

queue = [1]
seen = set()
vis_ord = []
while len(queue) != 0:
    fr = queue.pop(0)
    if fr not in vis_ord:
        print(fr)
        vis_ord.append(fr)
    for node in graph[fr]:
        if node not in seen:
            seen.add(node)
            queue.append(node)
        
print(vis_ord)
