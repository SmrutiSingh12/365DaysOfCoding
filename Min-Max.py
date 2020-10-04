#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/min-max-8/description/
n=int(input())
l1=list(map(int,input().split()))
l1.sort()
print(sum(l1[:n-1]),sum(l1[-(n-1):]))
