'''
@author: Abouelhassan Mohammed
'''
import random

def Transpose(Alpha):
    n=len(Alpha);m=len(Alpha[0])
    l= [[0 for _ in range(n)] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            l[j][i]=Alpha[i][j]
    return l

def RandomListBasedOn(Beta):
    oneIndexs=[index for index, value in enumerate(Beta) if value == 1]
    a=random.choice(oneIndexs)
    A=len(Beta)*[0]
    A[a]=1
    return A
#Beta=[1,0,0,1,0,1,0]
#print (RandomListBasedOn(Beta))


def generateRandomListX(Alpha):
    N=len(Alpha)
    l= [0 for _ in range(N)]

    for i in range(N):
        l[i]=RandomListBasedOn(Alpha[i])
    #print (l)
    return l
#Alpha=[[1, 0, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0]]
#print (generateRandomListX(Alpha))

def generateRandomListY(X):
    m=len(X);n=len(X[0])
    Y=[[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
    for j in range(m):
        for i in range (n):
            Y[j][i][i]=1
        oneIndexs=[index for index, value in enumerate(X[j]) if value == 1]
        k=len(oneIndexs)
        oneIndexs=random.sample(oneIndexs,k)
        for i in range(k):
            for e in range(i+1,k):
                Y[j][oneIndexs[i]][oneIndexs[e]]=1
    #print (Y)
    return Y
#X=[[1, 0, 1, 1], [1, 1, 0, 0]]
#print(generateRandomListY(X))



def PopGeneration(Npop,Alpha):
    X=[0 for _ in range(Npop)]
    Y=[0 for _ in range(Npop)]
    for i in range(Npop):
        A=generateRandomListX(Alpha)
        Y[i]=generateRandomListY(A)
        X[i]=(A)
    return (X,Y)

#Alpha=[[1, 0, 1, 1, 1, 0], [1, 1, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 1, 1]]
#print(PopGeneration(2,Alpha))*
#3Alpha=[[1, 0, 1, 1], [0, 1, 0, 0],[1, 1, 1, 1]]
#print(PopGeneration(1,Alpha))


#X=[[1, 0, 1, 1], [1, 1, 0, 0], [0, 1, 0, 0]]
#Y=[[[1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1]], [[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]
#P=[[[1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1]], [[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]
#T=[[2, 0, 1, 1], [1, 3, 0, 0], [0, 1, 4, 0]]

