import sys
import math
import heapq

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    input = sys.stdin.read
    data = input().splitlines()
    idx = 0
    results = []
    
    while True:
        # Read the number of players and finishing points
        N, M = map(int, data[idx].split())
        idx += 1
        if N == 0 and M == 0:
            break
        
        # Read players' positions and speeds
        players = []
        for _ in range(N):
            x, y, s = data[idx].split()
            players.append((int(x), int(y), float(s)))
            idx += 1

        # Read finishing points and acceptable colors
        finish_points = []
        for _ in range(M):
            *finish_info, _ = map(int, data[idx].split())
            x, y, *colors = finish_info[:-1]
            finish_points.append((int(x), int(y), colors))
            idx += 1

        # Prim-inspired approach to find minimum matching cost
        total_min_time = 0.0
        assigned_points = [False] * M  # Track if a finish point is assigned
        min_heap = []  # Min-heap to hold possible player-finish point pairs

        # Initialize the heap with possible connections for each player
        for i, (px, py, speed) in enumerate(players):
            for j, (fx, fy, accepted_colors) in enumerate(finish_points):
                if i + 1 in accepted_colors:  # i + 1 represents the player's color
                    distance = calculate_distance(px, py, fx, fy)
                    time = distance / speed
                    heapq.heappush(min_heap, (time, i, j))  # (time, player index, finish point index)

        # Track assigned players
        assigned_players = [False] * N

        # Process the heap to assign players to finish points
        while sum(assigned_players) < N:
            time, player, finish = heapq.heappop(min_heap)
            # Assign if neither the player nor the finish point has been used
            if not assigned_players[player] and not assigned_points[finish]:
                assigned_players[player] = True
                assigned_points[finish] = True
                total_min_time += time

        # Store the result rounded to 1 decimal place
        results.append(f"{total_min_time:.1f}")

    # Output all results for the test cases
    print("\n".join(results))
import sys
import math
import heapq

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    input = sys.stdin.read
    data = input().splitlines()
    idx = 0
    results = []
    
    while True:
        # Read the number of players and finishing points
        N, M = map(int, data[idx].split())
        idx += 1
        if N == 0 and M == 0:
            break
        
        # Read players' positions and speeds
        players = []
        for _ in range(N):
            x, y, s = data[idx].split()
            players.append((int(x), int(y), float(s)))
            idx += 1

        # Read finishing points and acceptable colors
        finish_points = []
        for _ in range(M):
            *finish_info, _ = map(int, data[idx].split())
            x, y, *colors = finish_info[:-1]
            finish_points.append((int(x), int(y), colors))
            idx += 1

        # Prim-inspired approach to find minimum matching cost
        total_min_time = 0.0
        assigned_points = [False] * M  # Track if a finish point is assigned
        min_heap = []  # Min-heap to hold possible player-finish point pairs

        # Initialize the heap with possible connections for each player
        for i, (px, py, speed) in enumerate(players):
            for j, (fx, fy, accepted_colors) in enumerate(finish_points):
                if i + 1 in accepted_colors:  # i + 1 represents the player's color
                    distance = calculate_distance(px, py, fx, fy)
                    time = distance / speed
                    heapq.heappush(min_heap, (time, i, j))  # (time, player index, finish point index)

        # Track assigned players
        assigned_players = [False] * N

        # Process the heap to assign players to finish points
        while sum(assigned_players) < N:
            time, player, finish = heapq.heappop(min_heap)
            # Assign if neither the player nor the finish point has been used
            if not assigned_players[player] and not assigned_points[finish]:
                assigned_players[player] = True
                assigned_points[finish] = True
                total_min_time += time

        # Store the result rounded to 1 decimal place
        results.append(f"{total_min_time:.1f}")

    # Output all results for the test cases
    print("\n".join(results))

main()