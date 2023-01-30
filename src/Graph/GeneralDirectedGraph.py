from collections import defaultdict
from sys import stdin


class DFS:
    """
    一般有向グラフにおける深さ優先探索の実装
    """    
    def __init__(self):
        N, M = map(int,stdin.readline().split())
        self._d = defaultdict(list)
        for _ in range(M):
            _input = stdin.readline().split()
            self._d[int(_input[0])].append(int(_input[1]))

        self._visited = [False]*N

    @property
    def d(self):
        return self._d

    def explore(self, route_output = False ,base = 0):
        if not self._visited[base]:
            if route_output:
                print(base)
            self._visited[base] = True
            for idx in self._d[base]:
                self.explore(route_output = True, base = idx)
                
    @property
    def visited(self):
        return self._visited

    def unreached_num(self):
        return len(self._visited) - sum(self._visited)

    def reached_num(self):
        return len(self._visited) - sum(self._visited)