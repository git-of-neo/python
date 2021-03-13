def paired_partition(lst):
    #swap if last digit is smaller than the first digit
    if lst[0]>lst[-1]:
        lst[0],lst[-1]=lst[-1],lst[0]
    p1=lst[0]
    p2=lst[-1]
    #tracker for the back and front part
    small_swap=1
    big_swap=len(lst)-2
    i=1
    end=len(lst)-1
    #end if i reaches location of p2
    while i<end:
        if lst[i]<p1:
            lst[i],lst[small_swap]=lst[small_swap],lst[i]
            small_swap+=1
        elif lst[i]>p2:
            lst[i],lst[big_swap]=lst[big_swap],lst[i]
            big_swap-=1
            end-=1
            i-=1
        i+=1
    #after sorting is done, move p1 and p2 to the end of
    #their respective paritition
    lst[0],lst[small_swap-1]=lst[small_swap-1],lst[0]
    lst[-1],lst[big_swap+1]=lst[big_swap+1],lst[-1]
    return lst
    
            

