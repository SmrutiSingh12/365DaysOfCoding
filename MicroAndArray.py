'''
problem Link:https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/description/
'''
count=0
l1=[]
tno=int(input())
for _ in range(0,tno):
    s1,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l1.sort()
    count=k-l1[0]
    if count<0:
       count=0
    print(count)
