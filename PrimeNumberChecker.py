#functon for check if a number is prime
def prime_checker(number):
  count =0
  for i in range(1,number+1):
    if number%i==0:
      count+=1
  if count==2:
    print('The number {0} is the prime number.'.format(number))
  else:
    print('The number {0} is not a primenumber'.format(number))


n = int(input("Check this number:"))
prime_checker(number=n)