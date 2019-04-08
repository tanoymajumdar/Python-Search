def applyMove(state, move):
    s=list(state)
    l=len(s)
    hol=[]
    i=0
    while (i<l):
        if(s[i]==0):
            if (move=="PUSH"):
                if (i!=0):
                    temp=0
                    temp=s[i]
                    s[i]=s[i-1]
                    s[i-1]=temp
                    return(tuple(s))
                else:
                    return(tuple(s))
            if (move=="PULL"):
                if (i!=l-1):
                    temp=0
                    temp-s[i]
                    s[i]=s[i+1]
                    s[i+1]=temp
                    return(tuple(s))
                else:
                    return(tuple(s))
            if (move=="SWAP"):
                if (i>1):
                    temp=0
                    temp=s[i-1]
                    s[i-1]=s[i-2]
                    s[i-2]=temp
                    return(tuple(s))
                else:
                    return(tuple(s))
            if (move=="FLIP"):
                if (i>l-2):
                    return(tuple(s))
                else:
                    temp=0
                    temp=s[i+1:l]
                    temp.reverse()
                    hol=s[0:i+1]
                    return(tuple(hol+temp))
        i=i+1
        
def h(state):
    s=list(state)
    p=0
    ha=0
    B=0
    C=0
    D=0
    for i in range(0,len(state)):
        if(s[i]==0):
            pac=len(state)-i
            break
        else:
            ha=ha+1
    A=ha*10
    for i in range (0,len(state)):
        if(s[i]==0):
            continue
        for j in range(i,-1,-1):
            if(s[j]==0):
                continue
            if(s[j]>s[i]):
                B+=1
                break
    for i in range (0,len(state)):
        if(s[i]==0):
            continue
        for j in range(i,len(state)):
            if(s[j]==0):
                continue
            if(s[j]>s[i]):
                C+=1
                break
    min1=B*17
    min2=(C*17)+8
    if(min1<min2):
        D=min1
    else:
        D=min2
    ha=D+A
    return ha
        
def getNext(frontier):
    min=1000
    mpos=0
    i=0
    while (i<len(frontier)):
        temp=0
        p=frontier[i]['path']
        hu=frontier[i]['state']
        hs=h(hu)
        for k in range(0,len(p)):
            if (p[k]=='PUSH'):
                temp=temp+10
            if (p[k]=='PULL'):
                temp=temp+5
            if (p[k]=='SWAP'):
                temp=temp+17
            if (p[k]=='FLIP'):
                temp=temp+8
        temp=temp+hs
        if (temp<min):
            min=temp
            mpos = i
        i=i+1
    return (frontier.pop(mpos))

    
def astarSearch(state):
  # initialize frontier using initial state of problem
  frontier = [ { 'state': state, 'path': [] } ]
  # while frontier is not empty
  while len(frontier) > 0:
    # choose a leaf node and remove it from frontier
    node = getNext(frontier)
 
    # if node contains a goal state
    if h(node['state']) == 0:
      # return corresponding solution
      return node['path']
 
    # expand the node adding the resulting nodes to the frontier
    for move in [ 'PUSH', 'PULL', 'SWAP', 'FLIP' ]:
      frontier.append( { 'state': applyMove(node['state'], move), 'path': node['path'] + [ move ] } )
 
  # return None if no solution is found
  return None
        
            
            
    
  
            
        
                    
                    
                
                
                    
            
                    
                    
                
                    
                
            