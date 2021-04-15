
l1=[45,23,43,67,12,1,2,3,]

def minmax(a,n):
    if(n==1):
        minmax.min=a[0]
        minmax.max=a[0]
        
        return minmax
    elif (n==2):
        if(a[0]>a[1]):
            minmax.min=a[1]
            minmax.max=a[0]
        else:
            minmax.min=a[0]
            minmax.max=a[1]
            
    
    minmax.min=minmax.max=a[0]
    for i in range(2,n):
        if a[i]>minmax.max:
               minmax.max=a[i]
        elif a[i]<minmax.min:
            minmax.min=a[i]
    return minmax
        
minmax1=minmax(l1,len(l1))        
print("min element:",minmax1.min)
print("max element :",minmax1.max)
    
