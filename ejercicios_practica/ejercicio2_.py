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

def listfjson(data, p1, p2, n):
    '''Filtra un JSON (data) y genera una y con los 
    valores de (p1) en base al valor de (p2)'''
    list_1 = [d[p1] for d in data if d[p2] == n ]
    return list_1

def listfrow(data, p1):
    '''Obtiene una y de un JSON (data) con los valores de 
    (p1) y los filtra con set para eliminar valores repetidos'''
    list_i = [d[p1] for d in data]
    list_m =set(list_i)
    list_f =list(list_m)
    return list_f

def bar_plot(x, y, lx, ly, t):
    '''Grafico de barras simple'''
    plt.bar(x,y)
    plt.ylabel(ly)
    plt.xlabel(lx)
    plt.title(t)
    plt.show()

def getinfo(data, p1, p2):
    '''Obtiene una lista con la suma de los valores de data[p2][p1]
     para cada item de la lista de valores de (p2)'''
    info = []
    klist = listfrow(data, p2)
    for n in klist:
        i = sum(listfjson(data, p1, p2, n))
        info.append(i)
    return info

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

x = listfrow(data, "userId")
y = getinfo(data, "completed", "userId")

print(x)
print(y)

bar = bar_plot(x, y, 'userId', 'Completed', 'ejercicio_2')

print("terminamos")
