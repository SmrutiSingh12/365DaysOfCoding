tno=int(input("Enter the no of test case"))
for _ in range(tno):
	s1=int(input("Enter the size of array"))
	l1=list(map(int,input().split()))
	l1.sort()
	if(l1[0]*l1[1]>l1[s1-1]*l1[s1-2]):
		print("Maximum sum:",l1[0]*l1[1],"is of",l1[0],l1[1])
	else:
		print("Maximum sum:",l1[s1-1]*l1[s1-2],"is of",l1[s1-1],l1[s1-2])