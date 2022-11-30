import random
def RS(tsp):
    C=list(range(len(tsp)))
    S=[]
    for i in range(len(tsp)):
        RC=C[random.randint(0,len(C)-1)]
        S.append(RC)
        C.remove(RC)
    return S
def RL(tsp,S):
    RL=0
    for i in range(len(S)):
        RL+=tsp[S[i-1]][S[i]]
    return RL
def GN(S):
    N=[]
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            neighbour=S.copy()
            neighbour[i]=S[j]
            neighbour[j]=S[i]
            N.append(neighbour)
    return N
def GBN(tsp,N):
    BRL=RL(tsp,N[0])
    BN=N[0]
    for neighbour in N:
        CRL=RL(tsp, neighbour)
        if CRL<BRL:
            BRL=CRL
            BN=neighbour
    return BN,BRL
def hillClimbing(tsp):
    CS=RS(tsp)
    CRL=RL(tsp,CS)
    N=GN(CS)
    BN,BNRL=GBN(tsp,N)
    while BNRL<CRL:
        CS=BN
        CRL=BNRL
        N=GN(CS)
        BN,BNRL=GBN(tsp,N)
    return CS,CRL
if __name__=="__main__":
    tsp = [[0,400,500,300],[400,0,300,500],[500,300,0,400],[300,500,400,0]]
    print(hillClimbing(tsp))
# week 3 Tic-Tac-Toe game