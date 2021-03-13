def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))

def hamiltonian(edges,path=[0],blocked=[]):
    options=boundary(edges,path,blocked)
    if 0 in options:
        return [path+[0]]
    else:
        res=[]
        for o in options:
            res+=hamiltonian(edges,path+[o],blocked+[(path[-1],o)])
        return res

def boundary(edges,path,blocked):
    res=[]
    for i in edges:
        if i not in blocked:
            L,R=i
            if L==path[-1]:
                res+=[R]
            if R==path[-1]:
                res+=[L]
    return res

E=[(0,1),(0,2),(0,3),(1,2),(1,3),(1,5),(2,4),(3,5),(4,5)]
print(hamiltonian(E))

