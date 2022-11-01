#%% 
def z_score(index , string, start = 0):
    k = start
    while index < len(string) and string[k] == string[index]:
        index+=1
        k+=1
    return k
        
def z_algo(string):
    z_array = [0]*len(string)
    z_array[0] = len(string)

    # (l, r)
    box = (0,0)

    for i in range(1, len(string)):
        # outside box
        if i>box[1]:
            z_array[i] = z_score(i, string)
            box = (i, i+z_array[i]-1) if z_array[i]>0 else (0,0)

        # inside box
        else:
            remaining = box[1] - i + 1
            k = i - box[0] 

            if z_array[k] < remaining:
                z_array[i] = z_array[k]

            elif z_array[k] > remaining:
                z_array[i] = remaining

            else:
                z_array[i] = z_score(box[1]+1, string, start = z_array[k])
                box = (i, i+z_array[i]-1) if z_array[i]>0 else (0,0)

    return z_array

def naive_z_algorithm(string):
    z_array = [0]*len(string)
    z_array[0] = len(string)
    for i in range(1, len(string)):
        z_array [i] = z_score(i, string)
    return z_array

def pattern_match(pat, text):
    z_array = z_algo(pat + "$" + text)
    matched = []

    for i in range(len(pat)+1, len(z_array)):
        if z_array[i] == len(pat):
            matched.append(i-len(pat)-1)
    
    return matched
# %%
