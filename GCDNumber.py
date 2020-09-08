def gcd(a,b): 
      
   
    if(b == 0):
    	return a 
    if(a==0):
    	return b
    if(a>b):
    	return gcd(b, a%b) 
    return gcd(b%a,a)
  

n=int(input("Enter the no of testcase:"))
for _ in range(n):
    a,b=map(int,input("Enter number:").split())
    print("GCD",gcd(a,b))