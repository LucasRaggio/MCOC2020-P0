from matplotlib import pyplot as plt
from scipy import  rand, float32,float64 , float16, zeros
from time import perf_counter 
import matplotlib 

N = 3 
A = ([[2,7,11],
      [16,20,25],
      [29,34,39]])
B = ([[3,5,6],
      [8,9,11],
      [12,14,15]])

#Aqui va la función NOTA: Le puse N para no gastar CPU en calcular el Len(A)

def mimatmul(A, B, N):                                        
    C= zeros((N,N) )    
    
    for i in range(N):
        for j in range(N):
            for k in range(N):            
                C[i][j] = C[i][j] + A[i][k]* B[k][j]
                
                

    return (C)
                
                
print (Producto(A,B,N))
