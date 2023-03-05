# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)
    
    def compute_subtree_height(node):
        if not nodes[node]:
            return 1
        subtree_heights = [compute_subtree_height(child) for child in nodes[node]]
        return 1 + max(subtree_heights)

    return compute_subtree_height(root)

def main():
    n = int(input().strip())

    parents = numpy.array(list(map(int, input().strip().split())))

    # call the function and output it's result
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
