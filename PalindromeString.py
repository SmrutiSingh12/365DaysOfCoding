n=input("Enter the string:")
n=n.lower()
n1=n
if(n1==n[::-1]):
	print(n,"is a palindrome string")
else:
	print(n,"is not a palindrome string")
