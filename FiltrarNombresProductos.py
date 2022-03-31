#datos
lista_productos = ['aseo', 'dulces', 'granos', 'dulces', 'verduras', 'dulces', 'aseo', 'granos', 'hogar']

lista_indices = [1, 4, 6, 3, 8]
nombre_producto = 'dulces'

lista_principal = ['aseo', 'verduras', 'granos', 'dulces', 'delicatessen', 'enseres']
lista_sucursal = ['licores', 'granos', 'electrodomésticos', 'aseo', 'ropa']

#variables del programa

#lista de productos sin repetir
def consultar_productos(lista_productos):
  lista=[]
  for item in lista_productos:
    if item not in lista:
      lista.append(item)
  return lista

#posicion de un elemento que coincida con la lista de indices
def consulta_posiciones_x_producto(lista_indices, lista_productos, nombre_producto):
  cont=0
  posicion=[]
  indices=[]
  for item in lista_productos:
    if nombre_producto==item:
      posicion.append(cont)
    cont+=1
  
  for i in lista_indices:
    for j in posicion:
      if i==j:
        indices.append(i)  
  return indices

#elementos de la sucursal que faltan en la lista principal
def consulta_productos_intercambio(lista_principal,lista_sucursal):
  num=0
  cont=0
  prod_intercambio=[]
  while(num<len(lista_principal)):
    for i in lista_sucursal:
      if lista_principal[num]!=i:
        cont+=1

    if cont==len(lista_sucursal):
      prod_intercambio.append(lista_principal[num])
    cont=0
    num+=1
  return prod_intercambio
  
#numero maximo de elementos a intercambiar
def consulta_max_productos_intercambio(lista_principal,lista_sucursal):
  num=0
  cont=0
  prod_intercambio=consulta_productos_intercambio(lista_principal,lista_sucursal)
  prod_intercambio2=[]
  while(num<len(lista_sucursal)):
    for i in lista_principal:
      if lista_sucursal[num]!=i:
        cont+=1

    if cont==len(lista_principal):
      prod_intercambio2.append(lista_sucursal[num])
    cont=0
    num+=1

  if len(prod_intercambio)<len(prod_intercambio2):
    return len(prod_intercambio)
  else:
    return len(prod_intercambio2)

#llamado de las funciones
print(consultar_productos(lista_productos))
print(consulta_posiciones_x_producto(lista_indices, lista_productos, nombre_producto))
print(consulta_productos_intercambio(lista_principal, lista_sucursal))
print(consulta_max_productos_intercambio(lista_principal, lista_sucursal))

