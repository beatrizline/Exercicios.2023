# Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles.
# Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn).
# Por exemplo, para as duas listas X e Y a seguir:

x = []
y = []
resposta = []
soma = 0
soma2 = 0

for i in range(5):
    a = int(input())
    x.append(a)

for i in range(5):
    um = int(input())
    y.append(um)

resultado = (x[0]*y[0])+(x[1]*y[1]+(x[2]*y[2])+(x[3]*y[3])+(x[4]*y[4]))

print(x)
print(y)
print(f'({x[0]} x {y[0]}) + ({x[1]} x {y[1]}) + ({x[2]} x {y[2]}) + ({x[3]} x {y[3]}) + ({x[4]} x {y[4]}) = {resultado}')
