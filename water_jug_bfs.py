from collections import deque

def bfs_water_jug():
    capA, capB = 4, 3
    start = (0, 0)
    goal = (2, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        # Goal test: (2,0)
        if (a, b) == goal:
            print()
            print("Breadth-First Search (BFS) algorithm :")
            for state in path:
                print(state)
            return

        successors = [
            (capA, b), # Filling Jug A
            (a, capB), # Filling Jug B
            (0, b),    # Empty Jug A
            (a, 0), # Empty Jug B
            (a - min(a, capB - b), b + min(a, capB - b)),  # Pour A → B
            (a + min(b, capA - a), b - min(b, capA - a))   # Pour B → A
        ]

        for s in successors:
            if s not in visited:
                queue.append((s, path))

bfs_water_jug()
