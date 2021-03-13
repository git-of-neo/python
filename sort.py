def selection_sort(lst):
    for i in range(len(lst)):
        cur=i
        for j in range(i,len(lst)):
            if lst[j]<lst[i]:
                cur=j
        lst[cur],lst[i] = lst[i] , lst[cur]
    return lst

lst=[4,8,5,7,10,-1]
print(selection_sort(lst))

def insertion_sort(lst):
    for i in range(1,len(lst)):
        if lst[i]<lst[i-1]:
            swap=i
            while swap>=1 and lst[swap]<lst[swap-1]:
                lst[swap],lst[swap-1] = lst[swap-1],lst[swap]
                swap-=1
    return lst

print(insertion_sort(lst))
print(insertion_sort([9,8,7,1,5]))

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        mid = len(lst)//2
        lst1=lst[:mid]
        lst2=lst[mid:]
        return merge(merge_sort(lst1),merge_sort(lst2))

def merge(lst1,lst2):
    res=[]
    i=0
    j=0
    while i<len(lst1) and j<len(lst2):
        if lst1[i]<lst2[j]:
            res+=[lst1[i]]
            i+=1
        else:
            res+=[lst2[j]]
            j+=1
    return res+lst1[i:]+lst2[j:]

print(merge_sort(lst))

def quick_sort(lst):
    if len(lst)<=1:
        return lst
    else:
        mid=partition(lst)
        left=lst[:mid]
        right=lst[mid+1:]
        return quick_sort(left)+[lst[mid]]+quick_sort(right)

def partition(lst):
    pivot=lst[0]
    i=1
    swap=1
    while i<len(lst):
        if lst[i]<pivot:
            lst[i],lst[swap]=lst[swap],lst[i]
            swap+=1
        i+=1
    swap-=1
    lst[swap],lst[0]=lst[0],lst[swap]
    return swap

print(quick_sort(lst))

lst2=quick_sort(lst)
def binary_search(lst,target):
    a=0
    b=len(lst)-1
    while a<=b:
        mid=(a+b)//2
        if lst[mid]==target:
            return mid
        else:
            if target>lst[mid]:
                a=mid+1
            else:
                b=mid-1
    return -1

print(binary_search(lst2,10))
            











