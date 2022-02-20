import random

ac=input("Votre prénom: ")
Consonnes=['qu','b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z']
Voyelles=['a','e','i','o','u','y']
Lan=['Français', 'Anglais', 'Espagñol', 'Italien', 'Allemand']
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
print("Bonjour %s, votre pseudo sera %s et il parlera %s" % (ac, pseudo, d))
