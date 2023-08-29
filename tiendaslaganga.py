# menu d opciones
# 1. Ingresar un producto en la bodega
# 2: verificar productos en bodega
# 3: buscar un porducto en la bodega
# 4: editar un producto en la bodega
# 5. retirar producto de la bodega
# 6: numero 6 salir

# producto: nombre, codigo, descripcion, foto, precio, cantidadEnbodega, fechaEntradaBodega

opc = 0
print("TIENDA EL GANGAZO")
print("***********************************")
print("Ingresar un producto en la bodega")
print("Verificar productos en bodega")
print("Buscar un porducto en la bodega")
print("Editar un producto en la bodega")
print("Retirar producto de la bodega")
print("Numero 6 salir")
print("***********************************")

productos = []

while opc != 6:
    producto = {}
    opc = int(input("Digita la opción deseada: "))
    if opc == 1:
        producto["nombre"] = input("digite el nombre del producto: ")
        producto["codigo"] = int(input("digite el codigo del producto: "))
        producto["descripcion"] = input("digite la descripción del producto: ")
        producto["foto"] = input("digite la URL de la foto: ")
        producto["precio"] = float(input("digite el precio del producto. "))
        producto["stock"] = int(input("digite el stock del producto: "))
        producto["fechaEntradaBodega"] = input("digite la fecha de entrada ")   
    elif opc == 2:
        for productoSeleccionado in productos:
            print(f"codigo = {productoSeleccionado['codigo']} ")
            print(f"nombre = {productoSeleccionado['nombre']} ")
            print(f"descripcion = {productoSeleccionado['descripcion']} ")
            print(f"Cantidad en bodega  = {productoSeleccionado['stock']} ")
            print(f"fecha de entrada en bodega = {productoSeleccionado['fechaEntradaBodega']} \n ")
            print(f"Precio = {productoSeleccionado['precio']} ")
    elif opc == 3:
        pass
    elif opc == 4:
        pass
    elif opc == 5 :
        pass
    elif opc == 6 :
        pass
    else:
        print("opción invalida, vuelva a intentarlo")


