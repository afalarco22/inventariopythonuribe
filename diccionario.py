productoTerminadoUno = {
    'referencia':5087,
    'marca':"Americanino",
    'descripcion': "Chompa de acampar",
    'color': "naranja",
    'costoUnitario': 100000,
    'disponibleBodega': True,
    'costoVenta': 850000,
    'puntosVentas':['cc mayorca', 'terminal norte', 'puerta el norte', 'centro de la moda']
    
}


productoTerminadoDos = {
    'referencia':5088,
    'marca':"Americanino",
    'descripcion': "camiseta polo",
    'color': "azul oscuro",
    'costoUnitario': 30000,
    'disponibleBodega': True,
    'costoVenta': 150000,
    'puntosVentas':['cc mayorca', 'terminal norte', 'puerta el norte', 'centro de la moda']
    
}

# creqando una lista de diccionarios

productos = [productoTerminadoUno, productoTerminadoDos]

# recorriendo una lista con un ciclo for

'''for i in range(1,10,2):
    print(i) '''
for producto in productos:
    for puntoVenta in producto["puntosVentas"]:
       print(puntoVenta)
       
    print("--------------------")
    
    
    
