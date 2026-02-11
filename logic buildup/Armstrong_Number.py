# Armstrong Number
# time complexity O(log_10(N))
import math

n = 153
num = n

count = int(math.log10(n)+1)
result = 0
while num>0:
    last_digit = num % 10
    result += last_digit ** count 
    num = num // 10

print(result)
if n == result:
    print("The Number is Armstrong")
else:
    print("The Number is Not Armstrong")