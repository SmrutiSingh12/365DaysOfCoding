l1=[1,2,3,4,5]



start=0
end=len(l1)

print("Before reverse:",l1)
def rev(l1, start, end):
    if start <= end:
        temp=l1[start]
        l1[start]=l1[end]
        l1[end]=temp
        rev(l1,start+1,end-1)
    return 
      
rev(l1,0,4)
print("After reverse:",l1)
