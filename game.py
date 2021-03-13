def num_mines(nested_list):
    #find '#'
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j]=='#':
                #prevent negative numbers 
                if i-1<0:
                    x=i
                else:x=i-1
                #prevent out of bounds
                while x<len(nested_list) and x<=i+1:
                    #prevent negative numbers 
                    if j-1<0:
                        y=j
                    else:y=j-1
                    #prevent out of bounds
                    while y<len(nested_list[i]) and y<=j+1:
                        #change the values in a 3x3 range excluding hashes
                        if nested_list[x][y]!='#':
                            if nested_list[x][y]=='-':
                                nested_list[x][y]='1'
                            else:
                                nested_list[x][y]=str(int(nested_list[x][y])+1)
                        y+=1
                    x+=1
    #convert remaining '-' to '0'
    for i in range(len(nested_list)):
        for j in range(len(nested_list[i])):
            if nested_list[i][j]=='-':
                nested_list[i][j]='0'
    return nested_list
