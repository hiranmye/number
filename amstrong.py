# your code goes here


lower,upper = map(int,raw_input("").split())

 
for num in range(lower,upper ):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num),
       num += 1
