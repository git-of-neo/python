def max_sum(lst):
    res=[]
    for i in range(len(lst)):
        res+=exe(lst,[lst[i]],i)
    cur=res[0]
    for i in res:
        if sum(i)>sum(cur):
            cur=i
    return [sum(cur),cur]

def exe(lst,part,v):
    options=increase(lst,part,v)
    if len(options)==0:
        return [part]
    else:
        res=[]
        for o in options:
            res+=exe(lst,part+[lst[o]],o)
        return res
        
def increase(lst,part,v):
    index=[]
    for i in range(v+1,len(lst)):
        if lst[i]>part[-1]:
            index+=[i]
    return index

print(max_sum([10,70,20,30,50,11,30]))
