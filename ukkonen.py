#%%
UNIQUE_CHARACTERS = 90 
STOP_CHAR = '$'

class Index:
    def __init__(self, index):
        self.index = index

    def increment(self):
        self.index+=1

class Edge:
    def __init__(self, start = None, end = None, suffix_link = None, payload = None):
        self.start = start if start!=None else Index(-1)
        self.end = end if start!=None else Index(-1)
        self.children = [None] * (UNIQUE_CHARACTERS+1)
        self.suffix_link = suffix_link
        self.payload = payload

    def length(self):
        return self.end.index - self.start.index

    def __str__(self):
        return "{} to {}".format(self.start.index, self.end.index)

def get_index(char):
    return ord(char) - ord(STOP_CHAR)

"""
Ukkonen algorithm for suffix tree building. Returns root node of suffix tree.

Space, Time O(N) where N is the length of text.
"""
def ukkonen(text):
    text+="$"
    root = Edge() # root edge has start=end=-1
    root.suffix_link = root
    active_edge = root
    active_length = 0
    last_j = -1
    global_end = Index(-1)

    for i in range(len(text)):
        global_end.increment()
        prev = root
        j = last_j + 1
        showstopper = False
        
        while j < i+1 and not showstopper:
            while True: 
                # p -> pointers, i -> children array indices
                p_current = j+active_length
                i_current = get_index(text[p_current])

                if active_edge.children[i_current] == None: # rule 2 case 1
                    # store suffix id at leaf
                    active_edge.children[i_current] = Edge(Index(p_current), global_end, root, payload = j)                    
                    last_j += 1
                    active_edge = active_edge.suffix_link # if suffix link not set up yet, defaulted to root
                    active_length = active_length - 1 if active_edge!=root else 0
                    break

                else:
                    next_edge = active_edge.children[i_current]
                    if j+ active_length + next_edge.length()<i: # skip count
                        active_length += next_edge.length()+1
                        active_edge = next_edge

                    else:
                        p_compare = next_edge.start.index + (i-p_current)
                    
                        if text[p_compare] == text[i]: # rule 3
                            showstopper = True
                        
                        else: # rule 2 case 2 
                            last_j +=1

                            internal_edge = Edge(next_edge.start, Index(p_compare-1), root) # create internal node
                            next_edge.start = Index(p_compare) # break leaf partially
                            internal_edge.children[get_index(text[p_compare])] = next_edge # remainder of broken leaf
                            internal_edge.children[get_index(text[i])] = Edge(Index(i), global_end, root, payload = j) # new leaf
                            active_edge.children[i_current] = internal_edge # attach leaf

                            # suffix link handling
                            if prev!=root:
                                prev.suffix_link = internal_edge
                            prev = internal_edge
                            active_edge = internal_edge.suffix_link # if suffix link not set up yet, defaulted to root
                            active_length = active_length - 1 if active_edge!=root else 0

                        break
            j+=1
    return root
    
# %% testing
# def print_tree(node: Edge, level = 0):
#     if node!=None:
#         if node.payload!=None:
#             print("leaf : ", node.payload)
#         childs = []
#         for j in range(len(node.children)):
#             i = node.children[j]
#             if i != None:
#                 if len(childs)==0:
#                     print("level : ", level)
#                 print(chr(ord('$')+j), end = " ")
#                 print(i)
#                 childs.append(i)
#         for kid in childs:
#             print_tree(kid, level+1)