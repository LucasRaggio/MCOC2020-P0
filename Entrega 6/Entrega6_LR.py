import numpy as np
import scipy as sp
from time import perf_counter
from matplotlib import pyplot as plt
from time import perf_counter 
from numpy import zeros
import matplotlib 
import scipy.linalg
from pylab import rcParams



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
     2,10,15,20,
      35,50,75,
      100, 200,300,
       500, 700,1000,
       1500,2000,3000 ,5000
    
       ,7500, 10000 ] #, 12000]


x_point   =   [10, 20, 50, 100, 200 , 500, 1000,2000, 3000,5000 , 7500, 10000] #,12000]

N_C= 10

Sin_Solver = []
Numpy_solver = []
Numpy_inv =[]
Scipy_inv =[]
Sp_Sol_OverOFF_gen = []
Sp_Sol_OverON_gen  = []
Sp_Sol_OverOFF_sym = []
Sp_Sol_OverON_sym=[]



for i in range(N_C): 
    dts_sinSolver = []
    dts_Numpy_solver = []
    dts_Numpy_inv =[]
    dts_Scipy_inv = []
    
    dts_Sp_Sol_OverOFF_gen=[]
    dts_Sp_Sol_OverON_gen =[]
    
    dts_Sp_Sol_OverOFF_sym =[]
    dts_Sp_Sol_OverON_sym = []
    
 
    for N in NE:
        
        A = matriz_laplaciana(N)
        B = np.ones(N)
        
        #Solucion a mano 1
        t1 = perf_counter()   
        A_i = np.linalg.inv(A)
        x = A_i@B
        t2 = perf_counter()
        dt = t2-t1
        dts_sinSolver.append(dt)
        
        
        #Solucion con numpy 2
        t1 = perf_counter()
        x = np.linalg.solve(A , B)
        t2 = perf_counter()
        dt = t2-t1
        dts_Numpy_solver.append(dt)
        
        #Solución con Numpy inv 3
        t1 = perf_counter()
        A_i = np.linalg.inv(A)
        x = A_i@B 
        t2 = perf_counter()
        dt = t2-t1
        dts_Numpy_inv.append((dt))
        
        #Solucion Scipy inv    4     
        t1 = perf_counter()        
        A_i = sp.linalg.inv(A)
        x = A_i@B 
        t2 = perf_counter()
        dt = t2-t1
        dts_Scipy_inv.append((dt))
        
        
        #Solucion scipy Overwrite off matriz generica 5 
        a = A
        b = B
        t1 = perf_counter()
        x = sp.linalg.solve(a, b, overwrite_a=False, overwrite_b=False , assume_a='gen')
        t2 = perf_counter()
        dt = t2-t1
        dts_Sp_Sol_OverOFF_gen.append(dt)
        
        
        #Solucion scipy Overwrite ON matriz generica 6 
        t1 = perf_counter()
        x = sp.linalg.solve(a, b, overwrite_a=True, overwrite_b=True , assume_a='gen')
        t2 = perf_counter()
        dt = t2-t1
        dts_Sp_Sol_OverON_gen.append(dt)
        
        
        #Solucion scipy Overwrite OFF matriz simetrica    7     
        t1 = perf_counter()
        x = sp.linalg.solve(a, b, overwrite_a=False, overwrite_b=False , assume_a='sym')
        t2 = perf_counter()
        dt = t2-t1
        dts_Sp_Sol_OverOFF_sym.append(dt)
        
        #Solucion scipy Overwrite ONNN matriz simetrica    8    
        t1 = perf_counter()
        x = sp.linalg.solve(a, b, overwrite_a=True, overwrite_b=True , assume_a='sym')
        t2 = perf_counter()
        dt = t2-t1
        dts_Sp_Sol_OverON_sym.append(dt)
        

        
    Sin_Solver.append(dts_sinSolver)
    Numpy_solver.append(dts_Numpy_solver)
    Numpy_inv.append(dts_Numpy_inv)
    Scipy_inv.append(dts_Scipy_inv)
    Sp_Sol_OverOFF_gen.append(dts_Sp_Sol_OverOFF_gen)
    Sp_Sol_OverON_gen.append(dts_Sp_Sol_OverON_gen)
    Sp_Sol_OverOFF_sym.append(dts_Sp_Sol_OverOFF_sym)
    Sp_Sol_OverON_sym.append(dts_Sp_Sol_OverON_sym)

    

def promedio(Lista_con_Listas):
    lista_promedio  = []
    
    for N in range(len(NE)):
        promedio = 0
        for i in range(N_C):
            promedio+= Lista_con_Listas[i][N]
        lista_promedio.append(promedio/N_C)
    
    return lista_promedio   
    
Pro_Sin_Solver          = (promedio(Sin_Solver))  
Pro_Numpy_solver        = (promedio(Numpy_solver))
Pro_Numpy_inv           = (promedio(Numpy_inv))
Pro_Scipy_inv           = (promedio(Scipy_inv))
Pro_Sp_Sol_OverOFF_gen  = (promedio(Sp_Sol_OverOFF_gen))
Pro_Sp_Sol_OverON_gen  = (promedio(Sp_Sol_OverON_gen))
Pro_Sp_Sol_OverOFF_sym  = (promedio(Sp_Sol_OverOFF_sym))
Pro_Sp_Sol_OverON_sym  = (promedio(Sp_Sol_OverON_sym))
  
 

       
y_time =       [0.1e-3  , 5* 0.1e-3, 1e-3 , 5* 1e-3 ,  1e-2  ,   0.1   ,  0.5   ,   1. ,  10.  ,  30   ,   60   , 60*10.  ]
y_time_text =  ['0.1 ms','0.5 ms'  ,'1ms' ,'5ms', '10 ms', '0.1 s' , '0.5 s','1 s' , '10 s','30 s', '1 min', '10 min' ]


rcParams['figure.figsize'] = 7, 10
plt.loglog(NE , Pro_Sin_Solver ,  '--o' , c= 'palegreen', label = 'Sin solver',linewidth=2 )
plt.loglog(NE , Pro_Numpy_solver ,  '--o' , c= 'c',  label = 'Numpy_solver',linewidth=2 )
plt.loglog(NE , Pro_Numpy_inv ,  '--o' , c= 'black',  label = 'Numpy_inv' ,linewidth=2)
plt.loglog(NE , Pro_Scipy_inv ,  '--o' , c= 'cornflowerblue',  label = 'Scipy_inv' ,linewidth=2)
plt.loglog(NE , Pro_Sp_Sol_OverOFF_gen ,  '--o' , c= 'orange',  label = 'Sp_Sol_OverOFF_gen' ,linewidth=2)
plt.loglog(NE , Pro_Sp_Sol_OverON_gen ,  '--o' , c= 'magenta',  label = 'Sp_Sol_OverON_gen' ,linewidth=2)
plt.loglog(NE , Pro_Sp_Sol_OverOFF_sym,  '--o' , c= 'gray',  label = 'Sp_Sol_OverOFF_sym',linewidth=2 )
plt.loglog(NE , Pro_Sp_Sol_OverON_sym,  '--o' , c= 'salmon',  label = 'Sp_Sol_OverON_sym',linewidth=2 )



plt.grid()   
plt.xticks( x_point, [])
plt.yticks( y_time , y_time_text)
plt.ylabel ('Tiempo transcurrido' , fontweight = 'bold')
plt.xlabel ('Diagonal de matriz [N]',  fontweight = 'bold' )
plt.title('Sistema de ecuaciones' , fontweight = 'bold')
matplotlib.rc('ytick', labelsize=12) 
matplotlib.rc('xtick', labelsize=12) 


plt.xticks( x_point, x_point, rotation = 90 )
  

plt.legend(loc= 'upper left', bbox_to_anchor=[0,1],
           ncol = 2, shadow=True, fontsize = 10, title = 'Metodo',
           fancybox=True)
plt.tight_layout() 



plt.savefig('Sistema de ecuaciones' ,dpi = 600) 






