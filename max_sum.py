def max_sum(lst):
    res=[]
    #find the list of subsequences with different starting point
    for i in range(len(lst)):
        part=[lst[i]]
        res+=recur_sum(lst,i,part)
    current=res[0]
    #find subsequence with largest sum
    for r in res:
        if sum(r)>sum(current):
            current=r
    #return [sum,subsequence]
    return [sum(current),current]

#the function below is adapted from lecture17 slide57
def recur_sum(lst,index,part):
    choices=options(lst,index)
    if choices==[]:
        return [part]
    else:
        res=[]
        for c in choices:
            res+=recur_sum(lst,c,part+[lst[c]])
        return res

#create list of index of elements that is larger than the element and in order
def options(lst,index):
    res=[]
    for i in range(index,len(lst)):
        if lst[i]>lst[index]:
            res.append(i)
    return res

    

