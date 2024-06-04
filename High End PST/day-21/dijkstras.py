from heapq import heappush, heappop
def dijkstras(graph, source, dest):
    distances = {}
    for vertex in graph:
        distances[vertex] = 999999
    distances[source] = 0
    queue = []
    heappush(queue, (0, source))
    while len(queue) != 0:
        cur_cost, cur_vertex = heappop(queue)
        if cur_cost > distances[cur_vertex]: continue
        '''
        1. add these 2 lines in case you want till destination only.
        2. remove the below 2 lines if you want source -> all vertices of graph
        '''
        if cur_vertex == dest:
            break
        for weight, node in graph[cur_vertex]:
            overall_cost = cur_cost + weight
            if overall_cost < distances[node]:
                distances[node] = overall_cost
                heappush(queue, (overall_cost, node))
    return distances
graph = {
    "A": [(2, "B"), (4, "D")],
    "B": [(1, "D"), (7, "C")],
    "C": [(1, "F")],
    "D": [(3, "E")],
    "E": [(2, "C"), (5, "F")],
    "F": [],
}
ans = dijkstras(graph, "A", "F")
print(ans)