def menu():
   
    print("1.Factorial \n")
    print("2.Palindrome \n")
    print("3.Exit \n")
    ch=(int)(input("Enter your choice:"))
    while ch!=4:  
        if ch==1:
            factorial()
        if ch==2:
            palindrome()
        if ch==3:
            exit()

 
def factorial():
    num=int(input("Enter number:"))
    fact=1
    i=1
    for i in range(i,num+1):
        fact=fact*i
    print("Factorial :",fact)
    menu()

def palindrome():
    inputString=input("Enter string:")
    if ((inputString[::-1])==inputString):
        print("Palindrome")
        menu()
    else:
        print("Invalid")
        menu()
menu()
