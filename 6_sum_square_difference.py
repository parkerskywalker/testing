"""
https://projecteuler.net/problem=6

El cuadrado de la suma de los diez primeros números naturales es
Halla la diferencia entre la suma de los cuadrados de los cien primeros números naturales y el cuadrado de la suma.
"""

sum_squares_final = 0 
lstSquares = []
sum_naturals = 0
difference = 0
for i in range(1, 101):        
    sum_naturals += i
    sum_squares_final += i**2    
    
difference = sum_naturals**2 - sum_squares_final
print(difference)



#338350
#25502500
#25164150