# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    adj_list = [[] for _ in range(n)]

    # Populate the adjacency list
    for i, parent in enumerate(parents):
        if parent != -1:
            adj_list[parent].append(i)

    def compute_node_height(node):
        if not adj_list[node]:
            return 0

        child_heights = [compute_node_height(child) for child in adj_list[node]]

        return max(child_heights) + 1

    return max(compute_node_height(root) for root in range(n) if parents[root] == -1)


def main():
    letter = input().strip()
    if letter == 'I':
        n = int(input().strip())
        parents = list(map(int, input().split()))
        print(compute_max_height(n, parents))
    elif letter == 'F':
        file = input().strip()
        file = "test/" + file
        if 'a' not in file:
            with open(file, 'r') as f:
                print(f.read())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()


