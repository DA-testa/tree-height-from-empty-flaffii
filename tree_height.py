# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    tree = [[] for _ in range(n)]

    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def calculate_height(node):
        heights = []
        for child in tree[node]:
            heights.append(calculate_height(child))
        if not heights:
            return 1
        return 1 + max(heights)

    max_height = calculate_height(root)

    return max_height

def main():
    n = int(input())

    parents_str = input()
    parents = list(map(int, parents_str.split()))

    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()

