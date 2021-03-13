def enough(cans,chosen):
    carb=[]
    protein=[]
    fat=[]
    #add the value of nutrition to their respective list
    for i in chosen:
        carb.append(cans[i][0])
        protein.append(cans[i][1])
        fat.append(cans[i][2])
    #requirements to achieve
    req1=sum(carb)>=500
    req2=sum(protein)>=250
    req3=sum(fat)>=90
    return (req1 and req2 and req3)

def to_take(cans):
    #below code for bitlists(n) and lex_suc(bitlist) adapted from lecture 11 page 30
    def bitlists(n):
        first = n*[0]
        last = n*[1]
        res = [first]
        while res[-1] != last:
            res += [lex_suc(res[-1])]
        return res

    def lex_suc(bitlst):
        res = bitlst[:]
        i = len(res) - 1
        while res[i] == 1:
            res[i] = 0
            i -= 1
        res[i] = 1
        return res
    
    def filter(cans,bitlist):
        chosen=[]
        #convert bitlist to list of index 
        for i in range(len(bitlist)):
            if bitlist[i]==1:
                chosen+=[i]
        if enough(cans,chosen):
            #add eligible index list to filtered_list
            filtered_list.append(chosen)

    filtered_list=[]
    res=bitlists(len(cans))
    #filter the bitlists for eligible bitlists
    for i in range(len(res)):
        filter(cans,res[i])
    current=filtered_list[0]
    for j in range(len(filtered_list)-1):
        #find index list with least amount of items 
        if len(filtered_list[j+1])<len(current):
            current=filtered_list[j+1]
    return current
            
        
