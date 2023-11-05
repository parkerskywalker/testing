class Factor():
    """
    https://projecteuler.net/problem=3

    The prime factors of 13195 are 5, 7, 13 and 29
    What is the largest prime factor of the number 600851475143

    Los factores primos de 13195 son 5, 7, 13 y 29
    ¿Cuál es el mayor factor primo del número 600851475143
    """
    
    def __init__(self):
        return None
    
    def __str__(self):
        return "Factor"


    def factorizar_numero(self, numero):
        factor = 2
        factores_primos = []
        while factor * factor <= numero:
            if numero % factor:
                factor += 1
            else:
                numero //= factor
                factores_primos.append(factor)
        if numero > 1:
            factores_primos.append(numero)
        return max(factores_primos)


numero = 600851475143
factor = Factor()
primos = factor.factorizar_numero(numero)
print(primos)
#print(f"Los factores primos de {numero} son: {factores_primos}")
