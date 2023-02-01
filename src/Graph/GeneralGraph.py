"""単純無向グラフの実装群"""
from collections import defaultdict
from sys import stdin

class DFS:
    """単純無向グラフでの深さ優先探索
    """    
    def __init__(self):
        N, M = map(int,stdin.readline().split())
        self._d = defaultdict(list)
        for _ in range(M):
            _input = stdin.readline().split()
            self._d[int(_input[0])].append(int(_input[1]))
            self._d[int(_input[1])].append(int(_input[0]))

        self._visited = [False]*N

    def explore(self, base = 0):
        if not self._visited[base]:
            self._visited[base] = True
            for idx in self._d[base]:
                self.explore(idx)

    @property
    def d(self):
        return self._d

    @property
    def visited(self):
        return self._visited

    def unreached_num(self):
        return len(self._visited) - sum(self._visited)

    def reached_num(self):
        return len(self._visited) - sum(self._visited)