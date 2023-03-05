# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    max_height = 0
    heights = [0] * n
    for vertex in range(n):
        if heights[vertex] != 0:
            continue
        height = 0
        i = vertex
        while i != -1:
            if heights[i] != 0:
                height += heights[i]
                break
            height += 1
            i = parents[i]
        max_height = max(max_height, height)
        i = vertex
        while i != -1:
            if heights[i] != 0:
                break
            heights[i] = height
            height -= 1
            i = parents[i]
    return max_height

def main():
    if len(sys.argv) == 1:
        n = int(input())
        parents = numpy.fromstring(input(), sep=' ', dtype=int)
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        if 'a' in filename:
            print("Error: filename contains 'a'")
            return
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = numpy.fromstring(f.readline(), sep=' ', dtype=int)
    else:
        print("Usage: python3 tree_height.py [filename]")
        return
    
    height = compute_height(n, parents)
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
