series = int(input('Enter a value'))
fibo = 0
num1 = 0
num2 = 1
while fibo < series+1:
    print(fibo,end=" ")
    fibo = num1 + num2
    num2 = num1
    num1 = fibo