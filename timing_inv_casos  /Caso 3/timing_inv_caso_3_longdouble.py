from matplotlib import pyplot as plt
from scipy import  rand 
from time import perf_counter 
import matplotlib 
from numpy import zeros

#from matplotlib.pylab import *
import scipy as sp
from scipy import linalg
import sys
import numpy as np



c = [ 'forestgreen' , 'royalblue' , 'turquoise' , 'cyan' , 'pink' , 'coral' , 
     'grey' , 'orange' , 'crimson' , 'teal']


NE = [ 
     2,5,8,10,12,16,20,
      25,30,35,40,45,
      50,60,70,80,90,
      100,125,150,175,
      200,250,300,350,
      400, 500, 600, 700,
      800, 900,1000,2000,
      3000]# [,4000, 5000]]


x_point            =   [10, 20, 50, 100, 200 , 500, 1000, 2000, 3000]   #Punto del grafico o

Corridas_dts = [] # Lista con los dts de cada corrida 
mem          = [] # Lista de la memoria consumida. 

N_C          = 3



def matriz_laplaciana(N, dtype):     
    A = zeros((N,N) , dtype = dtype)
    
    for i in range(N):
        for j in range(N):             
            if i == j:
                A[i,j]= 2                
            if i +1 == j:
                A[i,j]= -1                
            if i -1 == j: 
                A[i,j]= -1
                
    return A 



for i in range(N_C): 
    dts = []                                  #Resets de dts   
    
    for N in NE:                              # N pertenece a la lista de NE.
        a = matriz_laplaciana(N, np.longdouble)     # Multiplicacion de matrices.
        t1 = perf_counter()                   # Comienza el cronometro.        
        a_inv = sp.linalg.inv(a, overwrite_a = True)
        t2 = perf_counter()                   # Termina el cronometro.
        dt = t2 - t1                          # Tiempo transcurrido en la ejecucion de C
        dts.append(dt)
        
    Corridas_dts.append(dts)



for N in NE:    
    A = matriz_laplaciana(N, np.longdouble)
    m = (sys.getsizeof(A))
    mem.append(m)
    



y_time =       [0.1e-3, 1e-3, 1e-2, 0.1 , 1. , 10. , 60, 60*10.]
y_time_text =  ['0.1 ms', '1ms', '10 ms', '0.1 s' , '10 s', '1 min']



plt.subplot(2,1,1)

for i in range(N_C):
    plt.loglog(NE , Corridas_dts[i] , c[i]  )
    plt.loglog(NE , Corridas_dts[i] ,  'o' , c= c[i] )
    

plt.grid()   
plt.xticks( x_point, [])
plt.yticks( y_time , y_time_text)
plt.ylabel ('Tiempo de Op. [t]' , fontweight = 'bold')
plt.title('Timing_inv_caso_3_longdouble' , fontweight = 'bold')
matplotlib.rc('ytick', labelsize=8) 
    
    



y_GB = [ 10**3 , 10**4 , 10**5, 10**6 , 10**7 , 10**8, 10**9,8*10**9, 10**11]
y_GB_text = [ '1KB' , '10KB','100KB' , '1MB','10MB' , '100MB','1GB', '8GB', '100GB' ]


plt.subplot(2,1,2)
plt.loglog(NE , mem, c = c[9])
plt.loglog(NE , mem, 'o' , c = c[9])

plt.xticks( x_point, x_point, rotation = 90 )
plt.yticks( y_GB, y_GB_text)
plt.ylabel ('Uso en [Bytes] ' , fontweight = 'bold')
plt.xlabel ('Tamano de matriz [Diagonal]',  fontweight = 'bold' )
plt.grid()
matplotlib.rc('ytick', labelsize=8) 
matplotlib.rc('xtick', labelsize=6) 


plt.axhline(8000000000, linestyle = '--' , c ='red')

    
plt.savefig('timing_inv_caso_3_longdouble.png' ,dpi = 300)  