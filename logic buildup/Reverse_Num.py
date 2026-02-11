# Palindrome in Number
# Time Complexity = O(log_10(N))

n = 2332
num = n
result = 0

while num>0:
    last_digit = num % 10
    result = result * 10 + last_digit;
    num = num // 10

if n == result:
    print("The Number is Palindrom");
else:
    print("The NUmber is Not Palindrom")
