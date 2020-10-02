#Problem Link:https://www.hackerearth.com/practice/python/getting-started/input-and-output/practice-problems/algorithm/its-easy-1/description/
A,B,C=map(int,input().split())
temp=0
temp=A
A=B
B=temp
A=A*C
B=B+C
print(A,B)
