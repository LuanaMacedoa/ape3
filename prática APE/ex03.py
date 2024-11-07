n = int(input('Digite o valor de N: '))
x = int(input('Digite o valor de y: '))
y = int(input('Digite o valor de X: '))


for num in range(x, y + 1):
    if num % n == 0:
        print(num, end=" ")        