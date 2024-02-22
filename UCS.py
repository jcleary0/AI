import heapq

def valet_parking(graph, start, goal):
    # Priority queue to store nodes to be explored, ordered by path cost
    frontier = [(0, start, [start])]  # (cost, node, path)
    # Dictionary to keep track of explored nodes and their path costs
    explored = {start: 0}

    while frontier:
        # Pop node with the lowest path cost from the frontier
        cost, current_node, path = heapq.heappop(frontier)

        # Check if current node is the goal
        if current_node == goal:
            print("Path traced from start state to goal state:", "->".join(path))
            return cost

        # Explore neighbors of the current node
        for neighbor, edge_cost in graph[current_node].items():
            new_cost = cost + edge_cost
            new_path = path + [neighbor]

            # If neighbor is unexplored or the new path is cheaper
            if neighbor not in explored or new_cost < explored[neighbor]:
                explored[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor, new_path))

    # Goal not found
    return None


# Example graph represented as an adjacency list
parking_lot = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 7, 'E': 10},
    'C': {'A': 3, 'F': 6},
    'D': {'B': 7},
    'E': {'B': 10, 'F': 4},
    'F': {'C': 6, 'E': 4}
}

parking_lot2 = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'E': 6},
    'C': {'B': 3, 'F': 2},
    'D': {'A': 1, 'E': 7},
    'E': {'D': 7, 'B': 6, 'F': 5},
    'F': {'C': 2, 'E': 5}
}

start_space = 'A'  # Starting parking space
goal_space = 'E'  # Goal parking space

# Call valet_parking function
result = valet_parking(parking_lot2, start_space, goal_space)

if result is not None:
    print(f"Shortest distance from {start_space} to {goal_space} is {result} units")
else:
    print(f"No path from {start_space} to {goal_space} exists")
