from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple
import heapq

Graph = Dict[str, List[Tuple[str, float]]]  # node -> [(neighbor, weight), ...]


@dataclass
class VisitStep:
    current: str
    visited: List[str]
    frontier: List[str]
    note: str = ""


def bfs_steps(graph: Graph, start: str) -> List[VisitStep]:
    visited = set()
    queue = [start]
    steps: List[VisitStep] = [VisitStep(start, [], queue[:], note="Start BFS")]

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue

        visited.add(node)

        neighbors = [n for (n, _) in graph.get(node, [])]
        for n in neighbors:
            if n not in visited and n not in queue:
                queue.append(n)

        steps.append(VisitStep(node, sorted(list(visited)), queue[:], note="Visit node"))

    return steps


def dfs_steps(graph: Graph, start: str) -> List[VisitStep]:
    visited = set()
    stack = [start]
    steps: List[VisitStep] = [VisitStep(start, [], stack[:], note="Start DFS")]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)

        neighbors = [n for (n, _) in graph.get(node, [])]
        for n in reversed(neighbors):
            if n not in visited and n not in stack:
                stack.append(n)

        steps.append(VisitStep(node, sorted(list(visited)), stack[:], note="Visit node"))

    return steps


@dataclass
class DijkstraStep:
    current: str
    distances: Dict[str, float]
    visited: List[str]
    note: str = ""


def dijkstra_steps(graph: Graph, start: str) -> List[DijkstraStep]:
    dist: Dict[str, float] = {start: 0.0}
    visited = set()
    pq: List[Tuple[float, str]] = [(0.0, start)]

    steps: List[DijkstraStep] = [DijkstraStep(start, dict(dist), [], note="Start Dijkstra")]

    while pq:
        d, node = heapq.heappop(pq)
        if node in visited:
            continue

        visited.add(node)

        for neigh, w in graph.get(node, []):
            nd = d + w
            if neigh not in dist or nd < dist[neigh]:
                dist[neigh] = nd
                heapq.heappush(pq, (nd, neigh))

        steps.append(DijkstraStep(node, dict(dist), sorted(list(visited)), note="Relax edges"))

    return steps


def demo_graph() -> Graph:
    return {
        "A": [("B", 2), ("C", 1)],
        "B": [("D", 1), ("E", 3)],
        "C": [("D", 2), ("F", 4)],
        "D": [("E", 1)],
        "E": [("F", 1)],
        "F": [],
    }
