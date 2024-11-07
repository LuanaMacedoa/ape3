n = int(input('Digite o valor de N: '))
x = int(input('Digite o valor de y: '))
y = int(input('Digite o valor de X: '))

cont = 0
for num in range(x, y + 1):
    if num % n == 0:
        cont=cont + 1
print(cont)   


 