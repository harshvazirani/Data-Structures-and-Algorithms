import heapq
import sys
import math


def main():
    adj = [[] for _ in range(2001)]

    input = sys.stdin.readline()
    data = list(map(int, input.split()))
    M, A, B = data[0:3]
    for _ in range(M):
        input = sys.stdin.readline()
        data = list(map(int, input.split()))
        V1, W, V2 = data[0:3]
        adj[V1].append(Edge(V2, W))
        adj[V2].append(Edge(V1, W))

    dist = [math.inf for _ in range(2001)]
    dist[A] = 0
    dijkstra(adj, dist, A, B)


def dijkstra(adj, dist, A, B):
    done = [False for _ in range(2001)]
    pq = [PQElement(A, 0)]
    heapq.heapify(pq)
    while len(pq) != 0:
        u = heapq.heappop(pq).point
        if not done[u]:
            done[u] = True
            for E in adj[u]:
                v = E.destination
                if dist[v] > dist[u] + E.weight:
                    dist[v] = dist[u] + E.weight
                    heapq.heappush(pq, PQElement(v, dist[v]))
        if done[B]:
            print("YES")
            print(dist[B])
            break

    if not done[B]:
        print("NO")


class Edge:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight


class PQElement:
    def __init__(self, point, weight):
        self.point = point
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == '__main__':
    main()
