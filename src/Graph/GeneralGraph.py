from collections import defaultdict
from sys import stdin

class DFS:
    def __init__(self):
        N, M = map(int,stdin.readline().split())
        self._d = defaultdict(list)
        for _ in range(M):
            _input = stdin.readline().split()
            self._d[int(_input[0])].append(int(_input[1]))
            self._d[int(_input[1])].append(int(_input[0]))

        self._visited = [False]*N

    def d(self):
        return self._d