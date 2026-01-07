import heapq
def minheap(n):
    heapq.heapify(n)

def max_heap(n):
    n = [-x for x in n]
    heapq.heapify(n)
    return -heapq.heapify(n)