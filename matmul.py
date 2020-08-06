import scipy as sp


N  =  3

A  =  sp.matrix( sp.rand( N , N ))
B  =  sp.matrix( sp.rand( N , N ))

print ('Matriz aleatorea A' )
print ( A )
print ('')
print ('Matriz aleatorea B' )
print ( B )

C  =  A * B      # Ojo numpy esto es multiplicacion de arreglos

print ('\n')
print ('El resultado de la matriz A por la matriz B correspode a :' )
print ('\n')

print ( C )

#Tratemos de multiplicar otra matriz

A1 = sp.matrix(  [[1,2],
               [3,4]]   )

A2 = sp.matrix(  [[5,6],
               [6,8]]   )

print ('')

print ('Matriz aleatorea A1' )
print (A1)


print ('')
print ('Matriz aleatorea A2' )
print (A2)
print ('')


print ('')
print ('El resultado de la matriz A1 por la matriz A2 correspode a :' )
print ('')

print (A1 * A2) 
