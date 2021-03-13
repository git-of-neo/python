#%%
from math import log, floor

"""
Convert the list into a max heap

Time O(n log kn) where n is the number of elements in heap
and k is the complexity for comparing elements

Aux space O(n)
"""
def heapify(lst):
    heap = []
    for item in lst:
        insert(heap,item)
    return heap

"""
Move current node up the heap to its correct position

Time O(log kn) where n is the number of elements in heap
and k is the complexity for comparing elements

Aux space O(1)
"""
def rise(heap, current):
    item = heap[current]
    parent = (current-1)//2
    while parent>=0 and heap[parent]<item:
        heap[current] = heap[parent]
        parent, current = (parent-1)//2, parent
    heap[current] = item
    return heap

"""
Returns the level the current node is at
"""
def get_level(current):
    return int(floor(log(2*current + 2,2)))-1

"""
Returns index of smallest child of node

Time O(k) where k is the complexity for comparing elements

Aux space O(1)
"""
def find_max_child(heap, current):
    left_child = current*2+1
    right_child = current*2+2

    # no right child
    if current*2+2>=len(heap):
        return left_child
    elif heap[right_child] > heap[left_child]:
        return right_child
    else:
        return left_child

"""
Move current node down the heap to its correct position

Time O(log kn) where n is the number of elements in heap
and k is the complexity for comparing elements

Aux space O(1)
"""
def sink(heap, current):
    # while there is still at least one child to the node
    item = heap[current]
    while current*2+1 < len(heap):
        min_child = find_max_child(heap, current)

        if item < heap[min_child]:
            heap[current] = heap[min_child]
            current = min_child
        else:
            break
    heap[current] = item
    return heap
    
"""
Insert the item into the heap

Time O(log kn) where n is the number of elements in heap
and k is the complexity for comparing elements

Aux space O(1)
"""
def insert(heap, item):
    current = len(heap)
    heap.append(item)
    rise(heap, current)
    return heap

"""
Find the k smallest elements in the list

Time O(wn) where n is the number of elements in the list
and w is the complexity for comparing elements

Aux space O(k)
"""
def smallest_k_elements(lst, k):
    heap = []
    for item in lst:
        if len(heap)<k:
            heap = insert(heap, item)
        else:
            if heap[0]>item:    
                heap[0] = item
                heap = sink(heap, 0)
    return heap
        
#%%
"""
Verify that the given heap is indeed a max heap

Time O(n) where n is the number of elements in the heap

Aux space O(1)
"""
def is_heap(heap):
    for i in range(len(heap)):
        if 2*i+1 < len(heap) and heap[i] < heap[2*i+1]:
            print('failed')
        if 2*i+2 < len(heap) and heap[i] < heap[2*i+2]:
            print('failed')
       
# %%
lstA = [6,3,2,1,5,8,9,10]
is_heap(heapify(lstA))
print(smallest_k_elements(lstA, 3))
print(smallest_k_elements([],1))
print(smallest_k_elements([1000,1000,9999,9999,999,0,10001,0],5))
print(smallest_k_elements([-1,2,1,4,-6],3))
print('pass')

# %%
