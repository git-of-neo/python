def neighbours(string):
    for i in range(1,len(string)-1):
        #test for lowercase alphabets in between
        if string[i]>='a' and string[i]<='z':
            if string[i-1]!="+" or string[i+1]!="+":
                return False
        #test for lowercase alphabets at the first and last location
        if string[0]>='a' and string[0]<='z':
            return False
        if string[-1]>='a' and string[-1]<='z':
            return False
    return True
                
def repeated_pattern(string):
    #pattern at least repeated twice so, the pattern is at most half the string
    for i in range(1,len(string)//2):
        #starts range at two because the pattern must be repeated at least twice
        for j in range (2,len(string)):
            pattern=string[0:i+1:1]
            #checks if string comprised only of j number of the same pattern
            if string==j*pattern:
                return True
    return False

def palindromic(string):
    temp_store=[]
    store=[]
    for i in range(len(string)):
        for j in range(i,len(string)):
            #compares the string to the reversed string
            if string[i:j+1]==string[i:j+1][::-1]:
                temp_store=string[i:j+1]
                #store the longest palindrome
                if len(temp_store)>len(store):
                    store=temp_store
    return store
                
    
           
                
