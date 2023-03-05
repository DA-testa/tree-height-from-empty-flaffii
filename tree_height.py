# python3

import sys
import threading
import numpy as np


def compute_max_height(num_nodes, parents_list):
    children = {i: [] for i in range(num_nodes)}

    root_nodes = []
    for i, parent in enumerate(parents_list):
        if parent == -1:
            root_nodes.append(i)
        else:
            children[parent].append(i)

    def find_max_depth(node, depth):
        if not children[node]:
            return depth
        else:
            max_depth = 0
            for child in children[node]:
                child_depth = find_max_depth(child, depth+1)
                max_depth = max(max_depth, child_depth)
            return max_depth

    max_height = 0
    for root in root_nodes:
        height = find_max_depth(root, 0)
        max_height = max(max_height, height)
    return max_height + 1


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

