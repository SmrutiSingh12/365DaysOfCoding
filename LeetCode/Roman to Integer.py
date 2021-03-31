class Solution:
    def romanToInt(self, s: str) -> int:
        c=0
        s=list(s)
        b=len(s)
        for a in range(0,b):
            
            if s[a]=="I":
                c=c+1
              
                if(s[a+1:]==["V"]):
                    b=4
                
                    return b
                if(s[a+1:]==["X"]):
                    b=9
                
                    return b
            if(s[a]=="V"):
                d=5
                c=0
                p=0
                o=s[a+1:]
                j=0
                for j in range(0,len(o)):
                    if o[j]=="I":
                        c=c+1
                return d+c
            
            if(s[a]=="X"):
                d=10
                c=k=l=e=p=0
                
                o=s[a+1:]
                
                for j in range(0,len(o)):
                    if o[j]=="I":
                        c=c+1
                    if o[j]=="V":
                        e=5
                    if o[j]=="X":
                        
                        p=10
                        print(o[j:])
                        if o[j:]==["X"]:
                            p=p+10
                        
                    if o[j]=="L":
                        l=30
                    if o[j]=="C":
                        k=80
                print(d,c,e,p,l,k)
                return d+c+e+p+l+k
            
                
            if(s[a]=="L"):
                d=50
                c=k=l=e=p=0
                
                o=s[a+1:]
                
                for j in range(0,len(o)):
                    if o[j]=="I":
                        c=c+1
                    if o[j]=="V":
                        e=5
                    if o[j]=="X":
                        
                        p=10
                        p=p+10
                    if o[j]=="L":
                        l=30
                    if o[j]=="C":
                        k=80
                
                return d+c+e+p+l+k
                
            if(s[a]=="C"):
                d=100
                c=k=l=e=p=0
                
                o=s[a+1:]
                
                for j in range(0,len(o)):
                    if o[j]=="I":
                        c=c+1
                    if o[j]=="V":
                        e=5
                    if o[j]=="X":
                        p=10
                        if o[j+1:]==["X"]:
                            p=p+10
                    if o[j]=="L":
                        l=30
                    if o[j]=="C":
                        k=80
                print(d,c,e,p,l,k)
                return d+c+e+p+l+k
            if(s[a]=="D"):
                d=500
                return d
            if(s[a]=="m"):
                d=100
                return d
        return c 
