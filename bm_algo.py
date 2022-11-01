#%%
from z_algo_suffix import z_algo_suffix
from z_algo import z_algo

def build_mp_array(pat):
    array = z_algo(pat)
    array.append(0)
    # make sure that it is an exact prefix (try pat = "bba", text = "abababab")
    # for i in range(len(array)-2,0,-1):
    #     if array[i+1] > array[i]:
    #         array[i] = array[i+1]
    for i in range(len(array)-2,-1,-1):
        if array[i] + i != len(pat):
            array[i] = array[i+1]
    return array

def build_gs_array(pat):
    z_array_suffix = z_algo_suffix(pat)
    gs_array = [-1] * (len(pat)+1)
    #gs_array.append(len(pat))
    for i in range(len(pat)-1):
        j = len(pat) - z_array_suffix[i]
        gs_array[j] = i
    return gs_array
    
def build_bc_table(pat):
    # [] : char , [][] : index of pat
    # assume 26 possible characters (small cap a-z)
    BASE = ord('a')
    UNIQUE = 26
    bc_table = [None]*UNIQUE
    for i in range(len(pat)):
        # update current cell
        j = ord(pat[i]) - BASE
        if bc_table[j] == None:
            bc_table[j] = [-1]*len(pat)
        bc_table[j][i] = i

        # update cells at the back
        k = i + 1
        while k<len(pat) and bc_table[j][i] == 0:
            bc_table[j][k] = bc_table[j][k-1]
            k+=1
    return bc_table
    
def bm_algo(pat, text):
    mp_array = build_mp_array(pat)
    gs_array = build_gs_array(pat)
    bc_table = build_bc_table(pat)

    matched = []

    # right border of region of text
    m = len(pat)-1

    # galil mark for pat
    break_r = -1
    break_l = -1
    
    j = 0
    m = len(pat)

    while (j+m-1) < len(text):
        k = m-1
        
        while k>break_r and text[j+k] == pat[k]:
            k-=1
        
        if k==break_r:
            k = break_l -1
            while k>-1 and text[j+k] == pat[k]:
                k-=1
        
        # default shift
        shift = 1
        break_l = -1
        break_r = -1

        # mis match
        if k>-1:
            # bad character
            bc_shift = k - bc_table[ord(pat[k])-ord('a')][k]
            if bc_shift == k+1: # no match 
                shift = m
            elif bc_shift>shift:
                shift = bc_shift
            
            # matched prefix shift
            if gs_array[k+1] == -1:
                mp_shift = m-mp_array[k+1]
                if mp_shift > shift:
                    shift = mp_shift
                    break_r = mp_array[k+1]-1

            # good suffix shift
            else:
                gs_shift = m -1 - gs_array[k+1]
                if gs_shift > shift:
                    shift = gs_shift
                    break_r = gs_array[k+1]
                    break_l = gs_array[k+1] - (m-1-k) + 1
            
            # for debugging
            # print("J ", j, "shift ", shift, "bc ", bc_shift, "k ",k)
            # print("R ", break_r, "L ", break_l)

        # no mismatch
        else:
            shift = m-mp_array[1]
            matched.append(j)

        j+=shift
    
    return matched

# %%
pat = "baba" 
text = "abababab"
bm_algo(pat, text)

# %%
