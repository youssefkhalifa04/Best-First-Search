def best_first_search(graph, start, goal):
    """
    Implementation of the Best-First Search algorithm for a weighted graph.

    Args:
        graph: The graph represented as an adjacency dictionary
        start: The starting node
        goal: The goal node

    Returns:
        A tuple (path, total_cost) if a solution is found, (None, 0) otherwise
    """
    # Initialize the open list with the starting node
    # Format: (current_cost, node, path)
    open_list = [(0, start, [start])]
    visited = set()

    print(f"Initialization:")
    print(f"Open list: {[item for item in open_list]}")
    print(f"Visited nodes: {visited}\n")

    while open_list:
        # Sort the list by current cost (first element of the tuple)
        open_list.sort(key=lambda x: x[0])

        # Extract the node with the lowest cost
        current_cost, node, path = open_list.pop(0)

        # If this node is the goal, return the solution
        if node == goal:
            visited.add(node)
            print(f"Open list: {[item for item in open_list]}")
            print(f"Visited nodes: {visited}")
            print(f"Solution found: {' -> '.join(path)}, Total cost: {current_cost}")
            return path, current_cost

        # Skip if already visited
        if node in visited:
            continue

        # Mark as visited
        visited.add(node)

        # Generate successors
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_cost = current_cost + weight
                open_list.append((new_cost, neighbor, new_path))

        print(f"\nProcessed node: {node}")
        print(f"Open list: {[item for item in open_list]}")
        print(f"Visited nodes: {visited}")

    # If the list is empty and no solution was found
    print("\nFailure: no path found.")
    return None, 0


# Graph definition
graph = {
    'S': [('A', 5), ('B', 2), ('C', 4)],
    'A': [('D', 9), ('E', 4)],
    'B': [('G', 6)],
    'C': [('F', 2)],
    'D': [('H', 7)],
    'E': [('G', 6)],
    'F': [('G', 1)],
    'G': [],
    'H': []
}

# Run the algorithm
print("=== Best-First Search ===")
start_node = 'S'
goal_node = 'G'
solution_path, total_cost = best_first_search(graph, start_node, goal_node)

# Display results
if solution_path:
    print("\n=== Final Result ===")
    print(f"Optimal path: {' -> '.join(solution_path)}")
    print(f"Total cost: {total_cost}")
else:
    print("\nNo path found between the start node and the goal.")
