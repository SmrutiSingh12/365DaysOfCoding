s1=input("Enter str1:")
s2=input("Enter str2:")
s1=s1.lower()
s1=sorted(s1)
s2=s2.lower()
s2=sorted(s2)

if(s1==s2):
	print("Strings are anagram")
else:
	print("Strings are not anagram")


'''
Output:Enter str1:pqrs
Enter str2:Srqp
String are anagram

Enter str1:abc
Enter str2:pqrs
String are not anagram
'''