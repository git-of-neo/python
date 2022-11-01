def z_score_suffix(index , string, start = None):
    k = start if start!=None else len(string)-1
    while index >=0 and string[k] == string[index]:
        index-=1
        k-=1
    return len(string)-k-1

def z_algo_suffix(string):
    z_array = [0]*len(string)
    z_array[-1] = len(string)

    L = len(string) 
    R = len(string)

    for i in range(len(string)-2, -1, -1):
        # outside box
        if i < L:
            z_array[i] = z_score_suffix(i, string)
            L = i-z_array[i]+1
            R = i

        # inside box
        else:
            remaining = i-L+1
            k = len(string)-1-(R-i)

            if z_array[k] < remaining:
                z_array[i] = z_array[k]

            elif z_array[k] > remaining:
                z_array[i] = remaining

            else:
                z_array[i] = z_score_suffix(L-1, string, start = len(string) -1 - z_array[k])
                if z_array[i]>0:
                    L = i-z_array[i]+1
                    R = i
                else:
                    L = len(string)
                    R = len(string)

    return z_array