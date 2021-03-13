def balanced_brackets(string):
    opener=["{","[","("]
    closer=["}","]",")"]
    lst=[]
    for i in string:
        lst.append(i)
    record=[0,0,0]
    while len(lst)>0:
        cur=lst.pop()
        if cur in closer:
            type=closer.index(cur)
            record[type]-=1
        if cur in opener:
            type=opener.index(cur)
            record[type]+=1
        #if unmatched opener found,return False
        if record[type]>0:
            return False
    #if numbers do not match, return False
    for r in record:
        if r!=0:
            return False
    return True
    

    
                








