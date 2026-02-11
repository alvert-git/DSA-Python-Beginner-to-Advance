# Extracting Digits
# n = 5873

# while n>0:
#     last_digit = n%10
#     print(last_digit)
#     n = n//10

# Count Digits

# method 1
# time complexity O(log_10(N))
n1 = 5873

count = 0
while n1>0:
    count += 1;
    n1 = n1//10

print(f"the toal digits is {count}")

# method 2
# time complexity O(log_10(N))
import math 

n2 = 123213
print(f"the count of {n2} is {math.floor(math.log10(n2))+1}")