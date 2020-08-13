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
- Dividire en tres partes el grafico de tiempo de opercion, (1) Tamaño N matriz < 50, (2) Tamaño N matriz [50, 2000] y (3) Tamaño N matriz > 2000. 
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

En primer lugar se comparan los resultados de tiempo de operacion y uso de memoria  entre los difentes tipos de numeros utilizados en cada caso. 

  * Caso 1:  Se puede observar que los numeros double requieren de un mayor espacio. El tiempo de operacion es igual para ambos tipos de numeros. 
  * Caso 2:  Comparando la memoria se tiene que:  Half < Single < Double < Long double. Respecto al tiempo de operación se observa una leve diferencia siendo el más rapido Half,  Single,  Double y  Longdouble el más lento. 

