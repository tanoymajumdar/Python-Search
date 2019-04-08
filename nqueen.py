def countAttack(queen):
    count = 0
    for row1 in range( 0, len(queen) ):
        for row2 in range( row1 + 1, len( queen ) ):
            if queen[row1] == queen[row2]:
                count += 1
            elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                count += 1
    return count
    
def printMatrix(queen):
    q=list(queen)
    i=0
    while (i<len(q)):
        r=[]
        q=list(q)
        a=q[i]
        j=0
        while (j<len(q)):
            if q[i]!=j:
                q[i]=j
                t=countAttack(tuple(q))
                r.append(t)
                q[i]=a
            else:
                r.append('-')
            j=j+1
        for k in range(0,len(q)):
            print(r[k], end="  ")
        print()
        i=i+1
        
def moveOne(queen):
    q=list(queen)
    num=0
    minm=1000
    minp=0
    i=0
    while (i<len(q)):
        r=[]
        q=list(q)
        a=q[i]
        j=len(q)-1
        while (j>=0):
            if q[i]!=j:
                q[i]=j
                t=countAttack(tuple(q))
                if (t<minm):
                    minm=t
                    minp=j
                    num=i
                q[i]=a
            j=j-1
        i=i+1
    q[num]=minp
    return(tuple(q))
    
def printMatrix2(queen):
    q=list(queen)
    i=0
    while (i<len(q)):
        r=[]
        q=list(q)
        j=0
        while (j<len(q)):
            if (i==j):
                r.append('-')
            elif i!=j:
                t=0
                t=q[i]
                q[i]=q[j]
                q[j]=t
                v=countAttack(tuple(q))
                r.append(v)
                t=q[i]
                q[i]=q[j]
                q[j]=t
            
            j=j+1
        for k in range(0,len(r)):
            print(r[k], end="  ")
        print()
        i=i+1
        
def moveTwo(queen):
    q=list(queen)
    num=0
    minm=1000
    mini=0
    minj=0
    i=0
    while (i<len(q)):
        r=[]
        q=list(q)
        a=q[i]
        j=len(q)-1
        while (j>=0):
            if (i!=j):
                t=0
                t=q[i]
                q[i]=q[j]
                q[j]=t
                v=countAttack(tuple(q))
                if (v<minm):
                    minm=v
                    mini=i
                    minj=j
                t=q[i]
                q[i]=q[j]
                q[j]=t
            j=j-1
        i=i+1
    a=0
    a=q[mini]
    q[mini]=q[minj]
    q[minj]=a
    return(tuple(q))

    
            
        