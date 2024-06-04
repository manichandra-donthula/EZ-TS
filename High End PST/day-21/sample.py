# def BFS(graph, start):
#     visited = [start]
#     queue = [start]
#     while len(queue) != 0:
#         ele = queue.pop(0)
#         print(ele, end=", ")
#         for i in graph[ele]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)

def DFS(graph, start, visited = None):
    if visited == None:
        visited = set()
    visited.add(start)
    print(start, end="->")
    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            DFS(graph, i, visited)
graph = {
    0: [3, 2, 1],
    1: [0],
    2: [0, 4, 3],
    3: [0, 2],
    4: [2]
}
# BFS(graph, "A")
DFS(graph, 0)