def graph_from_file(file_name):
    file=open(file_name)
    #split by line then split by commas
    contents=list(map(lambda x:x.split(","),file.read().split("\n")))
    #convert strings to integer
    res=[]
    for i in contents:
        res.append(list(map(int,i)))
    return res

def valid_entry(vertex,graph,colored_vertex,color):
    for i in range(len(graph[vertex])):
        #find adjacent vertices
        if graph[vertex][i]==1:
            #check if any of the adjacent vertices have the chosen color
            if colored_vertex[i]==color:
                return False
    return True

def add_color_vertex(vertex,graph,colored_vertex,m):
    res=[]
    #if the color is valid add the new colored_vertex to res
    for i in range(1,m+1):
        if valid_entry(vertex,graph,colored_vertex,i):
            #create a copy of the colored_vertex then apply the color change
            change=colored_vertex[:]
            change[vertex]=i
            res+=[change]
    return res

def m_color(file_name,m):
    graph=graph_from_file(file_name)
    colored_vertex=[0]*len(graph)
    ans=solution(0,graph,colored_vertex,m)
    #if no plausible solution,return empty list
    if ans==None:
        return []
    return ans
    
def solution(vertex,graph,colored_vertex,m):
    #end recurssion when all are colored
    if vertex==len(graph):
        return colored_vertex
    else:
        options=add_color_vertex(vertex,graph,colored_vertex,m)
        for i in options:
            return solution(vertex+1,graph,i,m)







