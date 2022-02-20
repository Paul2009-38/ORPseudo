import random

Consonnes=['qu','b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z']
Voyelles=['a','e','i','o','u','y']
lanfin=""
pseudoV=[]
pseudo=""
for i in range(5):
    r=random.randint(1, 2)
    
    if r==1:
        n=0
        for i in Consonnes:
            n=n+1
        r=random.randint(1, n)
        pseudoV.append(Consonnes[r-1])
    else:
        n=0
        for i in Voyelles:
            n=n+1
        r=random.randint(1, n)
        pseudoV.append(Voyelles[r-1])

def defLan():
    n=0
    for i in Lan:
       n=n+1
    r=random.randint(1, n)
    return Lan[r]
d=defLan()
for a in range(5):
    pseudo=pseudo+pseudoV[a]
print("Votre pseudo sera %s" % (pseudo))
