# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
import requests

import matplotlib.pyplot as plt

def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data

def listfjson(data, para1):
    '''Filtra un JSON (data) y genera una lista en base a un parametro (para1)'''
    list_1 = [d[para1] for d in data]
    return list_1

def str_list(ini, fin, inte):
    '''Genera una lista de numeros en formato str'''
    l1 = list(range(ini, fin, inte))
    l2 = [str(x) for x in l1]
    return l2

def sum_list1(data, para1, para2):
    '''Divide una lista en (para2) y suma el calor de (para1) de la lista (data)'''
    w_list = listfjson(data, para1)
    n = para2
    sum_list = [sum(w_list[i:i + n]) for i in range(0, len(w_list), n)]
    return sum_list  

def bar_plot(x, y, lx, ly, t):
    plt.bar(x,y)
    plt.ylabel(ly)
    plt.xlabel(lx)
    plt.title(t)
    plt.show()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    data = extract(url)

    x = str_list(1, 11, 1)

    y = sum_list1(data, 'completed', 20)

print(x)
print(y)

bar = bar_plot(x, y, 'userId', 'Completed', 'ejercicio_2')

print("terminamos")