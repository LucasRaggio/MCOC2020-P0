# MCOC2020-P0
# E1 Mi computador 


Marca / Modelo : Macbook  Pro Touch  Bar 2017 

Tipo: Notebook 

Fecha de compra: 2018 

Sistema operativo: Apple MacOS Mojave

Procesador : 3,1 GHz intel core i5 -7276U

Memoria Ram:  8GB de 2133 Mhz  LPDDR3

Disco duro : 1 de 256 SSD 

Graficos: Intel iris plus graphics 650 1536 MB 

Cantidad de procesadores: 1 

Nucleos: 2 

Numero de Hilos: 4 

# E2 Desempeño MATMUL

![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Grafico.png?raw=true)


###### ¿Como difiere del gráfico del profesor/ayudante?
- Dividire en tres partes el grafico de tiempo de operción, (1) Tamaño N matriz < 50, (2) Tamaño N matriz [50, 2000] y (3) Tamaño N matriz > 2000. 
En la Zona 1 se puede obersar que mi computador tiene un tiempo de operación mayor. En la zona 2, tienen un comportamiento parecido y en la zona 3 la diferencia entre los tiempos de operacion es significativa (difieren por 20 s). 

- En el tiempo de operacion 

###### ¿A qué se pueden deber las diferencias?
- A los componentes del computador: 
  * Procesador: capacidad de ejecución, tipo de procesador, velcoidad del procesador (el mio es mas lento),numero de nucleo (el mio tiene 2 vs 4 del profe).
  * Tipo de Ram: Mi computador tiene menor RAM pero de mayor frecuencia.
  * Cantidad de Hilos. 
 


###### El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?

- El grafico de memoria mio con el de profesor son exactamente iguales. Esto es debido a que cada numero almacenado utiliza 8 Bytes de memoria. 

- La operación matricial (matriz de N x N) para encontrar cada termino que compone la matriz requiere de N operaciónes, por lo tanto, al ejecutar la multiplicaciones de matrices se hacen N^3 operaciones (multiplicaciones y suma). Las operaciones son diferentes ya que provienen de numeroes aleatoreos y deben guardarse en el programa. Sin embargo, la ram puede ser el cuello de botella.

- Mientras corria el programa realizaba otro trabajo el cual pudo haber afectado. 

###### ¿Qué versión de python está usando?
- 3.8 

###### ¿Qué versión de numpy está usando?
- 1.18.5

###### Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
- Tengo un solo procesador en mi mac. En mac no se puede ver. Solo se puede ver lo de la figura que se encuentra abajo. Se puede ver que el procesador se encuentra en 0% (en python) y al hacer correr el programa sube considerablemente hasta mantenerse constante. 


![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Procesador.png?raw=true)


# E3 MiMatmul 

## Utilizando la operacion A@B = C 

![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Grafico.png?raw=true)


## Utilizando la funcion mimatmul (a mano)

![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/G1_Matriz.png?raw=true)



## Se puede observar grandes diferencias 

  * 1) El calculo de la operacion A*B a mano en una matriz de 500 demora un 60.000% mas que el metodo anterior. 
  * 2) El calculo de la operacion A*B tiene una menor variacion de tiempos en cada corrida. 
  * 3) En matrices de tamaño diagonal menor a 5 el calculo a mano de la operacion A*B es mas efectivo en el tiempo. 


# CPU

# Utilizando la operacion A@B = C 
![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Procesador.png?raw=true)




## Utilizando la funcion mimatmul (a mano)
![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/CPU.png?raw=true)



## Se puede observar grandes diferencias 

  * 1) Se utiliza el doble de CPU en el calculo de la operación A@B 
  * 2) Se puede observar un pick Utilizando la funcion mimatmul pero esta se debe a otra aplicacion 
  * 3) La CPU utilizando la funcion mimatmul es mas constante. 

# E4 

![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/E4-1.png?raw=true)

Nota: En el caso uno, los numeros half y longdouble no son compatibles con numpy.

En primer lugar se comparan los resultados de tiempo de operación y uso de memoria  entre los difentes tipos de numeros utilizados en cada caso. 

  * Caso 1:  Se puede observar que los numeros double requieren de un mayor espacio. El tiempo de operación es igual para ambos tipos de números. 
  * Caso 2:  Comparando la memoria se tiene que:  Half < Single < Double < Long double. Respecto al tiempo de operación se observa una leve diferencia siendo el más rapido Half,  Single,  Double y  Longdouble el más lento. 
  * Caso 3: Ocurre exactamente lo mismo que en el caso 2. 
  
  
 En segundo lugar se comparan los resultados metodos utilizados. Caso 1 vs Caso 2 vs Caso 3
 
   * Se puede observar que utilizando numeros sigles el caso de menor teimpo de operacion es el 2, despues 3 y por ultimo el 1. 
   * En general no se puede observar grandes diferencies  en terminos de tiempo de operación en los casos. 


¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)?

  * Método 1: Diagonaliza la matriz inicial. 
  * Método 2 y 3:  Estos metodos utilizan la biblioteca de scipy.linalg, la cual contiene las funciones que numpy y algunas otras más. Para encontrar la inversa diagonaliza la matriz pero utilizando algoritmos numeros mas rápidos (minimos cuadrados). Compila utilizando otro soporte. 

  Fuente metodo 2 y 3 : https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html
  
  
  
  ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso?
  
  La computacion paralela puede hacer diferentes procesos al mismo tiempo. Esto sirve, por ejemplo resolver grandes problemas en muchos pequenos y resolverlos al mismo tiempo. La cache es la memoria  temporal que guarda los ratos para que se puedan procesar con una mayor rapidez. 
  
  En ambos casos se puede observar que cuando aumenta la memoria en uso lo procesos se vuelven mas lentos debido a que se acaba la memoria de cache y el computador utiliza memorias mas lentas. 
  
  En mi computador no se pueden ver la cantidad de procesadores activos. Por lo tanto es dificil hablar del desempeno en cada caso. 
  
  
Definción de velocidades segun memoria: 

  * Hay una jerarquía de velocidad en el computador. Disco duro es lo mas lento. Despues de la memoria ram. Cuando se excede la Ram el sistema trata de seguir procesando y lo que hace el computador es paginar el disco (es muy lento). Las caches es la memoria entre la memoria Ram y donde realmente ocurren los datos. Dentro de las memorias hay diferentes velocidades. El registro es la memoria que se encuentra en el procesador y es las MAS rapida de todas. 
  
  # Entrega 5 
  
  ![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Entrega%205/Sistema%20de%20ecuaciones.png?raw=true)
 
La figura anterior muestra el tiempo que demoran 2 metodos en resolver un problema con N incognitas. Se presenta que el metodo de dos pasos (calcula la inversa y multiplicación de matrices) es menos efectivo que el metodo ofrecido por la libreria numpy. 


# Entrega 6 

En esta entrega se utilizan diferentes metodos con diferentes opciones para resolver un sistema de ecuaciones Ax = b. Se utilizaron 7 metodos con 10 corridas, para valores de N (incognitas) de hasta 10.000.

## Métodos 
A continuación se describen los metodos utilizados. Metodo dos pasos = (Paso 1) Matriz inversa de A ;; (Paso 2) Innv_A * x.

  * Numpy_inv             : Método de dos pasos utilizando la libreria numpy. (np.linalg.inv(A))
  * Numpy_solver          : Se resuelve el sistema con un paso.               (x = np.linalg.solve(A , B))
  * Scipy_inv             : Metodo de dos pasos utilizando libreria scipy     (sp.linalg.inv(A))
  * Sp_Sol_OverOFF_gen    : Scipy con Overwrite Off y matriz general   sp.linalg.solve(a, b ,OFF, assume_a='gen')
  * Sp_Sol_OverON_gen     : Scipy con Overwrite ON  y matriz general   sp.linalg.solve(a, b ,ON,  assume_a='gen')
  * Sp_Sol_OverOFF_sym    : Scipy con Overwrite OFF y matriz simetrica sp.linalg.solve(a, b , OFF,  assume_a='sym')
  * Sp_Sol_OverON_sym     : Scipy con Overwrite ON y matriz simetrica  sp.linalg.solve(a, b, ON ,assume_a='sym')

  ![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Entrega%206/E6.png?raw=true)


###### Analisis de rapidez de los métodos utilizados:
Para el analisis se diviran los datos en 3 grupos. (1) Matrices pequeñas (N < 20), (2) Matrices medianas (20 < N < 500) y (3) Matrices grandes (N > 500)

Matrices pequeñas: No se presenta una clara diferencia entre los metodos de dos pasos y un paso. 
Matrices medianas: Diferencias en los tiempos de la libreria scipy vs numpy. La libreria numpy lidera en este tipo de matrices. 
Matrices grandes : Los métodos de dos pasos son considerablemente mas lentos (negra, azul y verde). No se presenta una gran diferencia entre la libreria de scipy vs la de numpy. 

###### CPU 

Al inicio del programa se utilizo un 270 % del procesador. Esto se debe a que se comienzan a importar las librerias.El computador enciende los ventiladors y el CPU se mantuvo constante en 198% al igual que en las entregas pasadas. Pareciera que los venntiladores no son capaces de infriar al procesador y disminuye la capacidad para evitar altas temperaturas. Luego de 20 min la CPU bajo hasta un 170% (Trabajaba para N = 5000), probablemente sea por la temperatura. 



# E7: Matrices dispersas y complejidad computacional 

## ❍ Complejidad algoritmica de MATMUL

  ![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Entrega%207/MATMUL.png?raw=true)

Diferencias  en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas:

  * Los tiempos de ensamblado son mas lentos en las matrices dispersas que las llenas debido a que se utilizo una funcion de matrices laplacianas optimizada. Esta función solo permitia generar la matriz laplaciana de manera llena por lo que para generar la matriz dispera se utilizaba un convertidor. Sin embargo, la diferencia es minima. (1 segundo para matriz de 10000)
  
  * Tanto como el tiempo de solucion y de ensamblado, las matrices dispersas tienen una menor variablidad en los tiempos. Disperda + Estable. 
  
  * El tiempo de solucion, hay una gran diferencia. Con matrices dispersas se obtiene la solución en 10 ms (N =10000) vs 10 segundos. 
  
  * El tiempo de solucion en las matrices dispersas se mantiene constante. 
  
  * Al utilizar matrices dispersas se requeire de menos recursos lo que se ve reflado en el tiempo de solucion. 
  

Complejidad asintotica para ensamblado y solucion: 

  * Para el ensamblado el comportamiento en ambos tipos de matrices es semejante (explicado en punto anterior). Cuando el N es muy grande, tiende a una complejidad   O(N^3).
  

  * En el tiempo de solucion, las matrices dispersas tienden a una complejidad O(N) vs O(N^3) en las matrices llenas. Esto se debe a que la matriz dispersa saca ventaja del gran numeros de ceros que tiene lo que hace que se utice menos memoria y recursos computacionales. 

¿Como afecta el tamaño de las matrices al comportamiento aparente?

  * Como ya se ha mencionado, para el tiempo de ensamblado se puede observar que para ambos tipos de matrices practicamente el mismo. Para valores de N< 20, a medida que aumenta el valor los tiempos de ensamble se reducen. Para N > 50, mientras aumenta el tamaño de la matriz tambien lo hace el tiempo. 
  
  * En el tiempo de ensamble y solución, para valores de N< 20 el tiempo decrece a medida que aumenta el tiempo. Esto se debe a que para ejecutar el programa, se requiere de realizar otras operaciones. 
  

Estabilidad de las corridas: 

  * Como ya se ha mencioado anteriormente, las matrices dispersas presentan una mayor estabilidad para las corridas que las llenas. Se puede observar que a medida que el tamaño de la matriz aumenta, la estabilidad tambien lo hace. Esto se debe a que para valores de N < 100, los tiempos de solucion y de ensamble son mucho mas pequenos que para N >1000, por lo que cualquier operacion extra en el computador afecta el rendimiento. 



## ❍ Complejidad algorítmica de SOLVE

  ![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Entrega%207/SOLVE.png?raw=true)
  
NOTA: El analisis de ensamble de matrices es exactamente el mismo que en Complejidad algorítmica de MATMUl. Para no aburrir al lector, solo se hablara del tiempo de solucion. 

Diferencias  en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas:

  * El tiempo de solución de matrices dispersas es mas estable que las matrices llenas. 
  
  * El tiempo de solución es menor cuando se utiza matrices dispersas. 
  
  * La solucion utilizando matrices dispersas tiene un complejidad computacional del orden O(N) vs O(N^3).

Complejidad asintotica para asamblado y solucion: 

  * Como se ha mencionado anteriormente, las matrices dispersas en tiempos de solución son considerablemente mas eficientes que las matrices llenas. 
  
  * Para valores grandes de N se tiene que la  complejidad computacional  para matrcies disperas es del orden O(N) vs O(N^3) de las matrcies llenas. 
  
  * Las matrices dispersas en el tiempo de solución para N < 1000 tienen una complejidad constante, es decir, para valores N pertenecientes entre 0 y 1000, independientemente del tamaño de la matriz, el tiempo de solución NO cambia considerablemente. 

¿Como afecta el tamaño de las matrices al comportamiento aparente?

  * Para matrices dispersas a medida que aumenta el N, el tiempo de solución no aumenta considerablemente. 
  
  * Se puede observar que para N = 10000, utilizando matrices dispersas el tiempo de solucion es solo de 9 ms. Lo cual es claramente mas eficiente que utilizando matrcies llenas (10 segundos de solucion). 
  
  * Para N < 100, las matrices llenas a medida que aumenta el valor de N, el tiempo decrece. Esto se puedr deber a que para ejecutar el programa, requiere de procesos extras. Para N > 200, la complejidad computacional aumenta con el valor de N. 
  

Estabilidad de las corridas: 

  * Las matrices dispersas son mas estables. 
  
  * Matrices llenas existe una mayor variabilidad debido a que estas guardan toda la informacion de la matriz. 
  
  
  
## ❍ Complejidad algorítmica de INV

  ![alt text](https://github.com/LucasRaggio/MCOC2020-P0/blob/master/Entrega%207/INV.png?raw=true)

Diferencias  en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas:

  * No presentan mayores diferencias entre las matrices utilizas para los tiempo, sin embargo, la pendiente de las matrices dispersas en el tiempo de solución es menos inclinada por lo que para matrices de tamaño > 10000, estas serian mas eficientes. 

Complejidad asintotica para asamblado y solucion: 

  * Para los tiempos de solución, la complejidad es del orden O(N^2.5) para matrices dispersas y  O(N^4) para matrices llenas. 

¿Como afecta el tamaño de las matrices al comportamiento aparente?

  * Como se espera y a sido en todos los casos de complejidad algoritmica estudiados, para tamaños pequeños de N (N<30) el tiempo de ensamble y de solución decrece con el tamaño de N. Luego, la complejidad aumenta tal como se menciono en el punto anterior. 

Estabilidad de las corridas: 

  * Como ya se ha mencionado en los puntos anteriores, las matrices dispersas son considerablemnte mas estables.
  



☛ Código de ensamblaje de la matriz laplaciana usada



☛ Comente cómo esta elección se ve reflejada en el desempeño y complejidad algorítmica mostrada.
  
  











