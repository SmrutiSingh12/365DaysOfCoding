#Problem Link:https://www.hackerearth.com/practice/python/getting-started/input-and-output/practice-problems/golf/jadoo-and-dna-transcription/description/

# Write your code here
str=input()
for i in str:
    if i!='G' and i!='C' and i!='T' and i!='A':
        print("Invalid Input")
        exit()
for i in str:

    if i=='G':
        print("C",end="")
    elif i=='C':
        print('G',end="")
    elif i=='T':
        print("A",end="")
    else:
        print('U',end="")


