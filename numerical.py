def continued_fraction(n):
    part1=[]
    part2=[]
    for i in range(1,(n+1)): #list up to n
        part1.append(i)
    for j in range (1,(n+2)): #list up to n+1
        part2.append(j)
    divisor=part1.pop()+part2.pop(-2)/part2.pop() #bottom most divisor
    while len(part1)>0:
        frac=part1.pop()+part2.pop()/divisor
        divisor=frac
    return (2+1/divisor)
        
#this one takes longer to load
def approx_pi(float):
    i=3
    count=4
    n=-1
    while i>0:
        count=count+n*(4/i)
        if (4/i)<float: #diffrence between current sum and previous sum is i/4
            return count
        n=n*-1
        i+=2

def smallest_difference(list1,list2):
    store=[]
    old_diff=0
    new_diff=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            new_diff=abs(list1[i]-list2[j])
            #calculate the difference and store the smallest difference
            if new_diff<old_diff and old_diff!=0:
                store=[list1[i],list2[j]]
                old_diff=new_diff
            #for the first difference where my old_diff is zero
            elif old_diff==0:
                old_diff=new_diff
                store=[list1[i],list2[j]]
            j+=1
        i+=1
    return store
   

                
        
        
        
        
    
            
