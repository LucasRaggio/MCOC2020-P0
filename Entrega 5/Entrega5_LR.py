
import numpy as np
import scipy as sp
from time import perf_counter
from matplotlib import pyplot as plt
from time import perf_counter 
from numpy import zeros


def matriz_laplaciana(N):
    A = zeros((N,N))
    
    for i in range(N):
        for j in range(N):             
            if i == j:
                A[i,j]= 2                
            if i +1 == j:
                A[i,j]= -1                
            if i -1 == j: 
                A[i,j]= -1
                
    return A 
    
NE = [ 
     2,5,8,10,12,16,20,
      25,30,35,40,45,
      50,60,70,80,90,
      100,125,150,175,
      200,250,300,350,
      400, 500, 600, 700,
      800, 900,950,1000,1500,2000,2500,3000,3500,
      4000, 4500 ,5000 , 6000, 7000,8000 , 9000, 10000]


x_point   =   [10, 20, 50, 100, 200 , 500, 1000,2000, 3000,4000,5000,10000]

N_C= 10 

Sin_Solver = []
Con_Solver = []



CV = ( [[1,2,3], [3,4,3], [3,2,4]])


for i in range(N_C): 
    dts_sinSolver = []
    dts_conSolver = [] 
    for N in NE:
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()   
        A_i = np.linalg.inv(A)
        x = A_i@B
        t2 = perf_counter()
        dt = t2-t1
        dts_sinSolver.append(dt)
        
        t1 = perf_counter()
        x = np.linalg.solve(A , B)
        t2 = perf_counter()
        dt = t2-t1
        dts_conSolver.append(dt)
        

        
    Sin_Solver.append(dts_sinSolver)
    Con_Solver.append(dts_conSolver)
    


   
        

def promedio(Lista_con_Listas):
    lista_promedio  = []
    
    for N in range(len(NE)):
        promedio = 0
        for i in range(N_C):
            promedio+= Lista_con_Listas[i][N]
        lista_promedio.append(promedio/N_C)
    
    return lista_promedio   
    
Pro_Sin_Solver = (promedio(Sin_Solver))  
Pro_Con_Solver = (promedio(Con_Solver))
  
 

       
y_time =       [0.1e-3, 1e-3, 1e-2, 0.1 , 1. , 10. , 60, 60*10. , 10*60*10 ]
y_time_text =  ['0.1 ms', '1ms', '10 ms', '0.1 s' , '1 s', '10 s', '1 min', '10 min' , '100 min']

plt.subplot(1,1,1)


plt.loglog(NE , Pro_Sin_Solver ,  '-o' , c= 'blue', label = 'Sin solver' )
plt.loglog(NE , Pro_Con_Solver ,  '-o' , c= 'red',  label = 'Con NP.solver ' )

plt.grid()   
plt.xticks( x_point, [])
plt.yticks( y_time , y_time_text)
plt.ylabel ('Tiempo de Op. [t]' , fontweight = 'bold')
plt.xlabel ('Tamano de matriz [Diagonal]',  fontweight = 'bold' )
plt.title('Sistema de ecuaciones' , fontweight = 'bold')


plt.xticks( x_point, x_point, rotation = 90 )

    

plt.legend()
plt.tight_layout()    
plt.savefig('Sistema de ecuaciones' ,dpi = 300) 