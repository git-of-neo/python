def bitlist(n):
    lst=[0]*n
    last=[1]*n
    res=[lst[:]]
    while res[-1]!=last:
        i=n-1
        while i>=0 and lst[i]==1:
            lst[i]=0
            i-=1
        lst[i]=1
        res+=[lst[:]]
    return res

print(bitlist(2))

def greedy_knapsack(weights,values,capacity):
    ratio=list(map(lambda x,y:x/y,values,weights))
    def score(i):return ratio[i]
    order=sorted(range(len(weights)),key=score,reverse=True)
    cur=0
    sel=[]
    for i in order:
        if weights[i]+cur<=capacity:
            sel+=[i]
            cur+=weights[i]
    return sel

weights = [4, 9, 10, 20, 2, 1]
values = [400, 1800, 3500, 4000, 1000, 200]
capacity = 20

print(greedy_knapsack(weights,values,capacity))

def perm(a,b):
    lst=[i for i in range(a,b)]
    last=lst[::-1]
    res=[lst[:]]
    while res[-1]!=last:
        i=len(lst)-2
        while i>=0:
            if lst[i]<lst[i+1]:
                break
            i-=1
        for j in range(i,len(lst)):
            if lst[j]>lst[i]:
                swap=j
        lst[i],lst[swap]=lst[swap],lst[i]
        lst=lst[:i+1]+lst[i+1:][::-1]
        res+=[lst[:]]
    return res

print(perm(1,4))

def brute_knapsack(weights,values,capacity):
    possible=bitlist(len(weights))
    res=[]
    for i in possible:
        if valid(i,capacity,weights):
            res+=[i]
    if len(res)==0:
        return "no solution"
    cur = res[0]
    for r in res:
        if value_of_bag(r,values)>value_of_bag(cur,values):
            cur=r
    return [cur,value_of_bag(cur,values)]
        
def valid(bitlist,capacity,weights):
    w=0
    for i in range(0,len(bitlist)):
        if bitlist[i]==1:
            w+=weights[i]
    if w<=capacity:
        return True
    return False

def value_of_bag(bitlist,values):
    res=0
    for i in range(0,len(bitlist)):
        if bitlist[i]==1:
            res+=values[i]
    return res

print(brute_knapsack(weights,values,capacity))







        
