from sys import stdin
from src.Graph import GeneralDirectedGraph
import pytest
from utility.mock_std import In, Out


def test_dfs_success_case(monkeypatch):
    stdin: object = In("tests/Graph/input/GeneralDirectedGraph_success_1.txt")
    stdout: object = Out("tests/Graph/output/GeneralDirectedGraph_success_1.txt")
    monkeypatch.setattr("sys.stdin.readline", stdin.pop)
    monkeypatch.setattr("sys.stdout.write", stdout.add)

    dfs=GeneralDirectedGraph.DFS()
    dfs.explore(route_output= True)
    assert stdout.outputs == stdout.validation
