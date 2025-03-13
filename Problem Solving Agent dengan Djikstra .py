import heapq

def dijkstra(graph, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            break
        
        for neighbor, weight in graph[current_node].items():
            new_cost = cost_so_far[current_node] + weight
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current_node
    
    return reconstruct_path(came_from, start, goal), cost_so_far.get(goal, float('inf'))

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# Contoh Graph (sama seperti yang digunakan pada DFS dan BFS)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 10},
    'C': {'A': 2, 'D': 3},
    'D': {'B': 5, 'C': 3, 'E': 2},
    'E': {'B': 10, 'D': 2}
}

# Menjalankan algoritma Dijkstra dari A ke E
path, cost = dijkstra(graph, 'A', 'E')
print("Path:", path)
print("Total Cost:", cost)
