class NaturalNumbers():
    """
    If we list all the natural numbers below 10 that are multiples 3 of or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    #2,3,5,7,11,13,17,19,23,29
    def primes(num):        
        for i in range(3, num):
            if num % i == 0:
                return "No", num            
        return "Si", num

    def multiple_of_divisor(num, divisor):
        if num % divisor == 0:
            return True
        return False 


sum = 0
natural = NaturalNumbers
for num in range(2, 1000):        
    if natural.multiple_of_divisor(num, 3) or natural.multiple_of_divisor(num, 5):
        sum += num
        print("{} {}".format(num, sum))

