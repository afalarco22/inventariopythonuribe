# menu d opciones
# 1. Ingresar un producto en la bodega
# 2: verificar productos en bodega
# 3: buscar un producto en la bodega
# 4: editar un producto en la bodega
# 5. retirar producto de la bodega
# 6: numero 6 salir

# producto: nombre, codigo, descripcion, foto, precio, cantidadEnbodega, fechaEntradaBodega

opc = 0
print("TIENDA EL GANGAZO")
print("***********************************")
print("1. Ingresar un producto en la bodega")
print("2. Verificar productos en bodega")
print("3. Buscar un producto en la bodega")
print("4. Editar un producto en la bodega")
print("5. Retirar producto de la bodega")
print("6. Numero 6 salir")
print("***********************************")

productos = [
    {
        "nombre": "Camisa",
        "codigo": 123,
        "descripcion": "Camisa tipo polo",
        "foto": "www.yahoo.es",
        "precio": 145000,
        "stock": 40,
        "fechaEntradaBodega": "12-12-2022"
    },

    {
        "nombre": "pantalon",
        "codigo": 456,
        "descripcion": "pantalon clásico",
        "foto": "www.yahoo.es",
        "precio": 250000,
        "stock": 23,
        "fechaEntradaBodega": "12-11-2022"
    }



]

while opc != 6:
    producto = {}
    print("Ha entrado en la opción 1")
    opc = int(input("Digita la opción deseada: "))
    if opc == 1:
        producto["nombre"] = input("digite el nombre del producto: ")
        producto["codigo"] = int(input("digite el codigo del producto: "))
        producto["descripcion"] = input("digite la descripción del producto: ")
        producto["foto"] = input("digite la URL de la foto: ")
        producto["precio"] = float(input("digite el precio del producto. "))
        producto["stock"] = int(input("digite el stock del producto: "))
        producto["fechaEntradaBodega"] = input("digite la fecha de entrada ")
        productos.append(producto)
    

    elif opc == 2:
        print("Ha entrado en la opción 2")
        for productoSeleccionado in productos:
            print(f'codigo = {productoSeleccionado["codigo"]} ')
            print(f"nombre = {productoSeleccionado['nombre']} ")
            print(f"descripcion = {productoSeleccionado['descripcion']} ")
            print(f"Cantidad en bodega  = {productoSeleccionado['stock']} ")
            print(f"fecha de entrada en bodega = {productoSeleccionado['fechaEntradaBodega']}")
            print(f"Precio = {productoSeleccionado['precio']} ")


    elif opc == 3:
        cod = int(input("Ingrese el código del producto que está buscando "))  

        for productoSeleccionado in productos:
            if cod == productoSeleccionado["codigo"]:
                print(f'codigo = {productoSeleccionado["codigo"]}')
                print(f"nombre = {productoSeleccionado['nombre']} ")
                print(f"descripcion = {productoSeleccionado['descripcion']} ")
                print(f"Cantidad en bodega  = {productoSeleccionado['stock']} ")
                print(f"fecha de entrada en bodega = {productoSeleccionado['fechaEntradaBodega']} ")
                print(f"Precio = {productoSeleccionado['precio']} ")
            else: pass
            
            
    elif opc == 4:
        cod = int(input("Ingrese el código del producto que quiere editar: "))
        for indice,producto in enumerate(productos):
            if cod == productos[indice]["codigo"]:
                productos[indice]["nombre"] = input("digite el nombre del producto: ")
                productos[indice]["codigo"] =  int(input("digite el codigo del producto: "))
                productos[indice]["descripcion"] = input("digite la descripción producto: ")
                productos[indice]["foto"] = input("digite la URL de la foto del prodcuto: ")
                productos[indice]["precio"] = float(input("digite el precio del producto: "))
                productos[indice]["stock"] = int(input("digite el stock del producto: "))
                productos[indice]["fechaEntradaBodega"] = input("digite fecha de llegada del producto: ")
            else: pass
       
    elif opc == 5 :

        cod = int(input("Ingrese el código del producto que quiere eliminar: "))  
        for productoSeleccionado in productos:
            if cod == productoSeleccionado["codigo"]:
                productos.remove(productoSeleccionado)   
            else: pass
        
    elif opc == 6 :
        pass
    else:
        print("opción invalida, vuelva a intentarlo")

print("ha salido del programa")



