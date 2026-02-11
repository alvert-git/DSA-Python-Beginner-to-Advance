#optimal solution for Prime number
from math import sqrt;

def prime_number(num):
    prime_factor=[]
    for i in range(1,int(sqrt(num))+1):
        if num%i == 0:
            prime_factor.append(i)
            if num//i != i:
                prime_factor.append(num//i)

    if len(prime_factor) <= 2 :
        print(f"The {num} is a prime number");
    else:
        print(f"The {num} is a not a prime number its divisor are {prime_factor}");

prime_number(7)