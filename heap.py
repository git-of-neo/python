def insert(heap,item):
    heap.append(item)
    cur=len(heap)-1
    par=(cur-1)//2
    while par>=0 and heap[par]>heap[cur]:
        heap[cur],heap[par] = heap[par],heap[cur]
        cur = par
        par = (cur-1)//2
    return heap

heap1=[4,9,11,15,18,13,14,17,18,23,20]
print(insert(heap1,10))

def extract_min(heap):
    heap[0] , heap[-1] = heap[-1] , heap[0]
    res  = heap.pop()
    cur=0
    while min_child(heap,cur) and heap[cur]>heap[min_child(heap,cur)]:
        a=min_child(heap,cur)
        heap[cur],heap[a]=heap[a],heap[cur]
        cur = a
    return res

def min_child(heap,i):
    if 2*i+1>=len(heap):
        return False
    if 2*i+2>=len(heap):
        return 2*i+1
    else:
        if heap[2*i+2]>heap[2*i+1]:
            return 2*i+1
        else:
            return 2*i+2

heap2=[4,11,10,15,18,11,14,17,19,23,20]
print("The min is {}".format(extract_min(heap2)))

def heap_sort(lst):
    heap=[]
    for i in lst:
        insert(heap,i)
    res=[]
    while len(heap)>0:
        res.append(extract_min(heap))
    return res

print(heap_sort([4,1,7,4,8,1,9]))


