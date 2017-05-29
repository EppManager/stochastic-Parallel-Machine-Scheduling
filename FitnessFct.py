'''
@author: Abouelhassan Mohammed
'''
import PopGeneration


def FitnessEval(X,Y,T,P):
    m=len(X);n=len(X[0]);l=m*[0]
    for j in range(m):
        A=0
        for i in range(n):
            A=A+X[j][i]*T[j][i]
            for k in range(n):
                A=A+X[j][i]*X[j][k]*Y[j][i][k]*P[j][i][k]
        l[j]=A
    return max(l)

#Npop=2
#Alpha=[[1, 0, 1, 1], [0, 1, 0, 0],[1, 1, 1, 1]]
#P=[[[1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1]], [[1, 0, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]]
#T=[[2, 0, 1, 1], [1, 3, 0, 0], [0, 1, 4, 0]]
#d=[88, 88, 88, 88]

def constraints(T,P,X,Y):
    m=len(X);n=len(X[0]);l=[]
    for k in range(n):
        A=0
        for j in range(m):
            for i in range(n):
                A=A+X[j][k]*Y[j][i][k]*(T[j][k]+P[j][i][k])
        l=l+[A]
    return l
#print (constraints(T,P,X,Y))


def feasibleSol(d,Npop,Alpha,T,P):
    A=[];n=len(Alpha[0])
    while len(A)<Npop :
        B=PopGeneration.PopGeneration(Npop,Alpha)
        B1=B[0];B2=B[1]
        #print (B1)
        #print (B2)
        for i in range(Npop):
            a=0
            K=constraints(T,P,B1[i],B2[i])
            while (a!=-1) and (a<n):
                if K[a]<=d[a]:
                    a=a+1
                else:
                    a=-1
            if (a!=-1):
                A=A+[(B1[i],B2[i])]
    return A


#print(feasibleSol(d,Npop,Alpha,T,P))






