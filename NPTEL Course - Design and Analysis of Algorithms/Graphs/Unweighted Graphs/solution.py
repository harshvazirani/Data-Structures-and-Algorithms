import sys
import math


def dfs(current_node, visited, adj):
    if not visited[current_node]:
        visited[current_node] = True
        for neighbour in adj[current_node]:
            dfs(neighbour, visited, adj)


def main():
    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    l, w, n = data[0:3]
    soldier = []
    visited = [False for _ in range(n + 2)]
    adj = [[] for _ in range(n + 2)]
    for i in range(n):
        input = sys.stdin.readline()
        data = list(map(int, input.split()))
        soldier.append(Point(data[0],  data[1]))
        if w-soldier[i].y <= 100:
            adj[n].append(i)
            adj[i].append(n)
        if soldier[i].y <= 100:
            adj[n+1].append(i)
            adj[i].append(n+1)

    for i in range(n):
        for j in range(i+1, n):
            if soldier[i].distance(soldier[j]) <= 200:
                adj[i].append(j)
                adj[j].append(i)

    dfs(n, visited, adj)
    print(int(visited[n+1]))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)


if __name__ == '__main__':
    main()