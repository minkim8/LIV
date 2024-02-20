import sys

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
         ]

MAX_LENGTH = len(graph[0])


# Input 0 if the start node and the end node are the same
for a in range(0, MAX_LENGTH):
    for b in range(0, MAX_LENGTH):
        if a == b:
            graph[a][b] = 0

# Calculating Floyd - Warshall Algorithm
for k in range(0, MAX_LENGTH):
    for a in range(0, MAX_LENGTH):
        for b in range(0, MAX_LENGTH):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# Printing the result
for a in range(0, MAX_LENGTH):
    for b in range(0, MAX_LENGTH):
        # When there is no path, print N
        if graph[a][b] == NO_PATH:
            print("N", end=' ')
        else:
            # Otherwise, print the shortest distance
            print(graph[a][b], end=' ')
    print()