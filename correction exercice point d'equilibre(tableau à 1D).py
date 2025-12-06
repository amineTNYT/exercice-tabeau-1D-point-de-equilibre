def poids2(t,k,n):
    s=0
    for i in range(k+1,n):
        s=s+t[i]
    return s
    
def poids1(t,k):
    s=0
    for i in range(k): 
        s=s+t[i]
    return s
    

def resultat(t,n):
    test=False
    for i in range(1,n-1):
        s1=poids1(t,i)
        s2=poids2(t,i,n)
        if s1==s2:
            print(i,"est un point d'équilibre")
            test=True
    
   
    if not(test):
        print("Aucun point d'équilibre")
    
