fizz_buzz = ["fizzbuzz" if num % 3 == 0 and num % 5 == 0 else "fizz" if num % 3 == 0 else "buzz" if num % 5 == 0 else num for num in range(1, 16)]
print(fizz_buzz)