"""
By listing the first six prime numbers: 2 3 5 7 11 13 we can see that the 6 th prime is 13
What is the 10001 st prime number?
"""
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

lst = []
target = 10001
for i in range(0, 120_000):
    if is_prime(i):                
        lst.append(i)
        
    try:
        if lst[target]:                        
            break
            
    except Exception as e:
        pass    

print(f"Index: {lst[target-1]}")
import ipdb; ipdb.set_trace()