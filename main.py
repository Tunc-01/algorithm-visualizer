from src.sorting_visualizer import main as run_sorting
from src.graph_algorithms import demo_graph, bfs_steps, dfs_steps, dijkstra_steps


def run_graph():
    g = demo_graph()

    print("\nGraph Algorithms (Demo Graph Nodes: A, B, C, D, E, F)")
    print("1) BFS")
    print("2) DFS")
    print("3) Dijkstra (Shortest Path)")

    choice = input("Choose: ").strip()
    start = (input("Start node (default A): ").strip().upper() or "A")

    if choice == "1":
        steps = bfs_steps(g, start)
        for s in steps:
            print(f"[BFS] current={s.current} visited={s.visited} frontier={s.frontier} | {s.note}")

    elif choice == "2":
        steps = dfs_steps(g, start)
        for s in steps:
            print(f"[DFS] current={s.current} visited={s.visited} frontier={s.frontier} | {s.note}")

    elif choice == "3":
        steps = dijkstra_steps(g, start)
        for s in steps:
            print(f"[Dijkstra] current={s.current} visited={s.visited} dist={s.distances} | {s.note}")

    else:
        print("Invalid choice.")


def main():
    print("\nAlgorithm Visualizer")
    print("1) Sorting Visualizer")
    print("2) Graph Algorithms")

    c = input("Choose: ").strip()

    if c == "1":
        run_sorting()
    elif c == "2":
        run_graph()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
