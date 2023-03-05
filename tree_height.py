# python3

import sys
import threading
import numpy


def compute_height(n, parents):

    nodes = [[] for i in range(n)]
    
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)
    

    def compute_height_rec(node):
        if not nodes[node]:
            return 1
        heights = [compute_height_rec(child) for child in nodes[node]]
        return 1 + max(heights)
    

    return compute_height_rec(root)


def main():

        filename = input("Enter filename: ")
        if 'a' in filename.lower():
            print("Error: File name cannot contain the letter 'a'.")
            return
        try:
            with open(f"input_files/{filename}", 'r') as f:
                n = int(f.readline())
                parents = numpy.fromstring(f.readline().strip(), sep=' ', dtype=int)
        except:
            print("Error: Invalid file name or format.")
            return

        print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
