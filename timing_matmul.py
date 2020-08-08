from matplotlib import pyplot as plt
from scipy import  rand 
from time import perf_counter 
import matplotlib 

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
     3000,4000, 5000]

Corridas_dts = [] # Lista con los dts de cada corrida 
mem          = [] # Lista de la memoria consumida. 

x_point            =   [10, 20, 50, 100, 200 , 500, 1000, 2000, 5000]   #Punto del grafico o
C_x_point_dts      = []                               #Lista con los dts de x_point




N_C          = 10  # N umero de corridas 


for i in range(N_C): 
    dts = []                         #Resets de dts
    C_x = []

       
    for N in NE:                     # N pertenece a la lista de NE.    
        A  =  rand( N , N )          # Genero la matriz aleatorea A.
        B  =  rand( N , N )          # Genero la matriz aleatorea B.
        t1 = perf_counter()          # Comienza el cronometro.        
        C = A@B                      # Multiplicacion de matrices.
        t2 = perf_counter()          # Termina el cronometro.
        dt = t2 - t1                 # Tiempo transcurrido en la ejecucion de C
        dts.append(dt)
        
        
    for i in x_point:        
        r1 = NE.index(i)
        t =  dts[r1]
        C_x.append(t)

    C_x_point_dts.append(C_x)
    Corridas_dts.append(dts)  
    
    

A, B ,C = 0,0,0 

      

for N in NE: 
    Memoria = 3*(N**2)*8         # 3 matrices por numero de numeros por 8 bytess.
    mem.append(Memoria)    
     
        #1KB = 10^3 Bytes
        #1MB = 10^3 KB
        #1GB = 10^3 MB

m = []        
for i in x_point: 
    r1 = NE.index(i)
    t =  mem[r1]
    m.append(t)
    
     

# Ya se tienen las listas que se deben graficar. 


y_time =       [0.1e-3, 1e-3, 1e-2, 0.1 , 1. , 10. , 60, 60*10.]
y_time_text =  ['0.1 ms', '1ms', '10 ms', '0.1 s' , '10 s', '1 min']



plt.subplot(2,1,1)

for i in range(N_C):
    plt.loglog(NE , Corridas_dts[i] , c[i] )
    plt.loglog(x_point , C_x_point_dts[i] ,  'o' , c[i] )
    

plt.grid()   
plt.xticks( x_point, [])
plt.yticks( y_time , y_time_text)
plt.ylabel ('Tiempo de Op. [t]' , fontweight = 'bold')
plt.title('Rendimiento A@B = C' , fontweight = 'bold')
matplotlib.rc('ytick', labelsize=8) 






y_GB = [ 10**3 , 10**4 , 10**5, 10**6 , 10**7 , 10**8, 10**9, 10**10, 10**11]
y_GB_text = [ '1KB' , '10KB','100KB' , '1MB','10MB' , '100MB','1GB' , '10GB', '100GB' ]

plt.subplot(2,1,2)
plt.loglog(NE , mem, c = c[9])
plt.loglog(x_point , m , 'o' , c = c[9])

plt.xticks( x_point, x_point, rotation = 90 )
plt.yticks( y_GB, y_GB_text)
plt.ylabel ('Uso en [Bytes] ' , fontweight = 'bold')
plt.xlabel ('Tamano de matriz [Diagonal]',  fontweight = 'bold' )
plt.grid()
matplotlib.rc('ytick', labelsize=8) 
matplotlib.rc('xtick', labelsize=6) 

plt.savefig('filename.png' ,dpi = 500)



