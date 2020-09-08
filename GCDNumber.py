def gcd(a,b): 
      
    # Everything divides 0  
    if (b == 0): 
         return a 
    return gcd(a, a%b) 
  

n=int(input("Enter the no of testcase:"))
for _ in range(n):
    a,b=map(int,input("Enter number:").split())
    print("GCD",gcd(a,b))