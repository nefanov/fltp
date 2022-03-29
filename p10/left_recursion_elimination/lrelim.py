n=int(input("Input number of productions:"))

Sym=[]
V=[]
T=[]
P=[]
for i in range(n):
    prod=input("Input production of the form L->R1|R2|..|..:")
    v=prod[0]
    if v not in V:
        V.append(v)
        P.append([])
    ind=V.index(v)
    for j in range(3, len(prod)):
        if(prod[j] not in Sym):
            Sym.append(prod[j])
    lst=prod[3:].split('|')
    for z in lst:
        P[ind].append(z)
for j in Sym:
    if j not in V:
        T.append(j)

print(T)
print(V)
print(P)

#Eliminate indirect recursion

l=len(V)
for i in range(l):
    for j in range(i):
        for p in P[i]:
            if(p[0]==V[j]):
                for k in P[j]:
                    P[i].append(k+p[1:])
                P[i].remove(p)


for i in range(len(V)):
    res=V[i]+'->'+P[i][0]
    for j in range(1,len(P[i])):
        res+='|'+P[i][j]
    print(res)

#Eliminate direct recursion

for i in range(l):
    flag=0
    for j in P[i]:
        if(j[0]==V[i]):
            flag=1
            break
    if(flag==1):
        V.append(V[i]+'\'')
        P.append([])
        j=0
        l=len(P[i])
        while(j<l):
            if(P[i][j][0]==V[i]):
                P[len(P)-1].append(P[i][j][1:]+V[i]+'\'')
            else:
                if(P[i]=='ε'):
                    P[i].append(V[i]+'\'')
                else:
                    P[i].append(P[i][j]+V[i]+'\'')
            P[i].remove(P[i][j])
            l-=1
        P[len(P)-1].append('ε')

            
print(V)
print(P)

print("Result grammar:")
for i in range(len(V)):
    res=V[i]+'->'+P[i][0]
    for j in range(1,len(P[i])):
        res+='|'+P[i][j]
    print(res)
