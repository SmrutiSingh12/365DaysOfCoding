'''
Problem Link:https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/vc-pairs/description/

'''
n=int(input())

a1=['a','e','i','o','u']
for _ in range(n):
    count=0
    n=int(input())
    str1=input()
    for i in range(0,n-1):
        if(str1[i] not in a1 and str1[i+1] in a1):
            count=count+1
    print(count)
