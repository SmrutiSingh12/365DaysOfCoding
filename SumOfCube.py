tno=int(input())
for _ in range(tno):
    s1=[]
    l1=list(map(int,input().split()))
    for item in l1:
        q=item**3
        s1.append(q)
        
    print(sum(s1),end=" ")
