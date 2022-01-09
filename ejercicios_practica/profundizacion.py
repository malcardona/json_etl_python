# Ejercicios de práctica [Python]

##

import json
import requests

import matplotlib.pyplot as plt

def extract(url):
    # Extraer el JSON de la URL pasada
    # como parámetro
    response = requests.get(url)
    data = response.json()
    return data

def cur_ars(data, var, curr):
    dat = data[var]
    dat_ars = [x for x in dat if x[curr] == "ARS"]
    return dat_ars

def fetch(data, p1, p2):
    k_list = [ p1 , p2 ]
    da_set = [{k:v for (k,v) in x.items() if k in k_list} for x in data]
    return da_set

def transform(data, p1, min, max):
    minl = [x[p1] for x in data if x[p1] < min]
    medl = [x[p1] for x in data if (x[p1] > min and x[p1] < max) ]
    maxl = [x for x in data if x[p1] > max]
    min_count = len(minl)
    min_max_count =len(medl)
    max_count = len(maxl)
    return [min_count, min_max_count, max_count]

def pie_plot(data, v1,v2 , v3):
    dat = data
    lab = [v1, v2, v3]
    plt.pie(dat, labels=lab, autopct="%0.1f %%")
    plt.show()

if __name__ == "__main__":

    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'

    data1 = extract(url)

    ars = cur_ars(data1, "results", "currency_id")
    #print(ars)

    dataset = fetch(ars, "price", "condition")

    data2 = transform(dataset, "price", 5000, 30000)

    report = pie_plot(data2, "<$5.000", ">$5.000 & <$30,000", ">$30.000")
    

