# What is the sum of the digits of the number 2^1000?

number = 2**1000
number = str(number)
sum_number = 0
for i in range(0,len(number),1):
    sum_number += int(number[i])
print(sum_number)
