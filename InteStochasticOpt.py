'''
@author: Abouelhassan Mohammed
'''
import FitnessFct



def ProblemSol(Npop,Alpha,T,P,d):
    I=[]
    A=FitnessFct.feasibleSol(d,Npop,Alpha,T,P)
    N=len(A)
    B=[]
    for i in  range(N):

        B=B+[FitnessFct.FitnessEval(A[i][0],A[i][1],T,P)]

    Z=[i[0] for i in sorted(enumerate(B), key=lambda x:x[1])]
    R=[i[1] for i in sorted(enumerate(B), key=lambda x:x[1])]
    for i in range(N):
        I=I+[(R[i],A[Z[i]][0],A[Z[i]][1])]

    return  I
