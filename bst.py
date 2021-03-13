def height(bst,v=0):
    if v is None:
        return -1
    left,right=bst[v]
    return max(height(bst,left),height(bst,right))+1

tree = [(1,2),(3,4),(5,6),(None,7),(8,None),(9,10),
(None,None),(None,None),(None,None),(None,None),(None,None)]
print(height(tree))

def search(bst,target,labels,v=0):
    if v is None:
        return -1
    if labels[v]==target:
        return v
    left,right=bst[v]
    if target>labels[v]:
        return search(bst,target,labels,right)
    else:
        return search(bst,target,labels,left)

labels = [12,8,18,3,10,15,20,5,9,13,16]
print(search(tree,5,labels))


def insert(bst,target,labels,v=0,path=[]):
    if v is None:
        left,right=bst[path[-1]]
        labels.append(target)
        bst.append((None,None))
        if target>labels[path[-1]]:
            right = len(bst)
            bst[path[-1]] = left,right
        else:
            left = len(bst)
            best[path[-1]] = left,right
        print(bst)
        print(labels)
        return
    left,right = bst[v]
    if target>labels[v]:
        insert(bst,target,labels,right,path+[v])
    else:
        insert(bst,target,labels,left,path+[v])

bst=[(1,2),(3,4),(5,6),(8,9),(10,11),(None,None),(None,None),(None,None),(None,None),(None,None),(None,None)]
labels=[24,20,28,15,22,26,30,14,17,21,23]
insert(bst,27,labels)





