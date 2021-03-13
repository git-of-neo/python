def find_missing(list):
    front=0
    back=len(list)-1
    #shrink the list until the missing segment is found
    while back-front!=1:
        middle=(back+front)//2
        #the missing part is in the part with higher average difference
        if (list[middle]-list[front])/(middle-front)>(list[back]-list[middle])/(back-middle):
            diff=list[back]-list[back-1]
            back=middle
        else:
            diff=list[front+1]-list[front]
            front=middle
    return list[front]+diff

def local_valley(list):
    front=0
    back=len(list)-1
    found=False
    while not found:
        mid=(front+back)//2
        #look for valleys (smaller than neighbours)
        if list[mid]<list[mid+1] and list[mid]<list[mid-1]:
            return list[mid]
        elif mid-1<0 and list[mid]<list[mid+1]:
            return list[mid]
        elif mid+1==len(list) and list[mid]<list[mid-1]:
            return list[mid]
        #move to the side with smaller number(valleys are small numbers)
        elif list[mid-1]<list[mid]:
            back=mid-1
        elif list[mid+1]<list[mid]:
            front=mid+1
    
