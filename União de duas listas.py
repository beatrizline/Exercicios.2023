# Faça um programa que leia duas listas de 10 elementos.
# Crie uma lista que seja a união entre as 2 listas anteriores, ou seja, que contêm os números das duas listas.
# Não deve conter números repetidos.

def eliminar_repetidos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    print(elementos_unicos)

def main():
    a = []
    b = []
    x = []

    for i in range(10):
        n = int(input())
        a.append(n)

    for i in range(10):
        k = int(input())
        b.append(k)

    for i in range(10):
        x.append(a[i])

    for i in range(10):
        x.append(b[i])

    eliminar_repetidos(x)

if __name__ == '__main__':
    main()
