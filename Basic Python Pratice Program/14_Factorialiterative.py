'''factorial n! - n* n-1*n-2..1'''

def fac_iterative_method(n):
    fac = 1
    for i in range(n):
        fac = (fac * (i+1))
        print('fac of',i+1,'=',fac)
        
number = int(input('enter the number'))
fac_iterative_method(number)


