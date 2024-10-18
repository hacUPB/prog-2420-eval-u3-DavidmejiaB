# Diccionario global donde se almacena datos de las prendas
prendas_dict = {}
# Se agrega al diccionario global información de la clave prenda
def agregar_prenda_dict(prenda, talla, precio, color):
    prendas_dict[prenda] = {
        'talla': talla,
        'precio': precio,
        'color': color
    }
# Se imprimirá cada una de las prendas    
def imprimir_prendas_dict():
    for prenda in prendas_dict:
        print(prenda)
# Buscar las prendas próximas a solicitud
def buscar_prendas_dict(prenda_buscada):
    if prenda_buscada in prendas_dict:
        datos = prendas_dict[prenda_buscada]
        print(f"prenda: {prenda_buscada}, talla: {datos['talla']}, precio: {datos['precio']}, color: {datos['color']}")
    else:
        print(f"Prenda: '{prenda_buscada}' no encontrada.")
# Agregamos las prendas
agregar_prenda_dict('camisa', 'S, M, L', 10000, 'azul')
agregar_prenda_dict('pantalón', 'S, M, L, XL',150000, 'verde')
agregar_prenda_dict('boxers', 'S, M', 21000, 'cafe')
agregar_prenda_dict('Medias', 'M, XL',21000, 'rojo')
agregar_prenda_dict('zapatos', '32, 33, 40',310000, 'rojo, verde, negro, blanco')
agregar_prenda_dict('gafas', 'marco único',35000, 'negras')
# Imprimimos las prendas
print("Nombres de las prendas:")
imprimir_prendas_dict()
solicitud= input("Qué penda desea ")
# Buscamos una prenda
if solicitud == 'camisa':
    buscar_prendas_dict('camisa')
    print("Se encuentra en el pasillo 1, columna 1")
elif solicitud =="pantalón":
    buscar_prendas_dict('pantalón')
    print("Se encuentra en el pasillo 1, columna 2")
elif solicitud =="boxers":
    buscar_prendas_dict('boxers')
    print("Se encuentra en el pasillo 1, columna 3")
elif solicitud =="medias":
    buscar_prendas_dict('medias')
    print("Se encuentra en el pasillo 2, columna 1")
elif solicitud =="zapatos":
    buscar_prendas_dict('zapatos')
    print("Se encuentra en el pasillo 2, columna 2")
elif solicitud =="gafas":
    buscar_prendas_dict('gafas')
    print("Se encuentra en el pasillo 2, columna 3")
