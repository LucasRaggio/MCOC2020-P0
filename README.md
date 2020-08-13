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





