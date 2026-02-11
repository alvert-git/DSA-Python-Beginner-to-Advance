# Brute force
def factor(n):
    result = [];
    for i in range(1,n+1):
        if n%i == 0:
            result.append(i)
    return result 


# factors_number = factor(10)
# print(factors_number)

# Better solution

def better_factor(n):
    result=[];
    for i in range(1,(n//2)+1):
        if n%i == 0:
            result.append(i);
    result.append(n);
    return result;

# factors_number = better_factor(20);
# print(factors_number)


# Optimal SOlution
from math import sqrt


def optimal_solution(num):
    result = []
    for i in range(1,int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)

        if i != num // i:
            result.append(num // i)

    result.sort()
    return result

print(optimal_solution(36))