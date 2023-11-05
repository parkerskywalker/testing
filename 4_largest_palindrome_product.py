"""
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
    9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.

    Un número palindrómico se lee igual en ambos sentidos. El mayor palíndromo formado por el producto de dos números de 2 cifras es 9009 = 91 x 99.
    Encuentra el palindromo más largo hecho del producto de 
"""    

class PalindromeNumber():
    #def __init__(self, x, y):
    #    self.x = x
    #    self.y = y

    def __str__(self):
        return "Palindrome "
    
    def get_number(self, x, y):           
        return x * y
    
    def get_palindrome(self, number):
        word = str(number)           

        lst = []
        reversed = []
        for letter in word:
            lst.append(int(letter))
        
        reversed = lst[::-1]
        
        if lst == reversed:
            return (number)


lst = []
object = PalindromeNumber()
for x in range(100, 999, 1):
    for y in range(100, 999, 1):        
        number = object.get_number(x, y)        
        palindrome = object.get_palindrome(number)  
        if palindrome is not None:            
            lst.append(palindrome)    

print(max(lst))

