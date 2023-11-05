"""
https://projecteuler.net/problem=5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

2520 es el número más pequeño que se puede dividir por cada uno de los números del 1 al 10 sin que quede ningún resto.
¿Cuál es el número positivo más pequeño que es divisible por todos los números del 1 al 20? ?

"""
class SmallestNumber():
    #def __init__(self, number):
    #    self.number = number        

    #def __str__(self, number):
    #    return self.number
    
    def operation(self, number, sequence):
        lst = []        
        for i in range(1, sequence):            
            if number % i == 0:
                if number not in lst:
                    lst.append(number)
            else:
                if number in lst:
                    lst.remove(number)                    
                    break
            
            #print(f"{sequence} ... { number }%{ i }={ number % i }")
        for fields in lst:
            return fields
        #return lst

number = 1000000000000
sequence = 20
lst = []
smallest = SmallestNumber()
for i in range(number, 1, -1):    
    response = smallest.operation(i, sequence)
    if response is not None:
        print(f"{response}")
        lst.append(response)

print(lst)