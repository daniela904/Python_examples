import json
suma=0

prod_disponibles= input("Ingrese productos que están disponibles para la venta en la tienda: ")
#'''{"mango": 9852, "pan": 4920, "coco": 6488, "ajo": 9711, "papa": 14396}'''

prod_comprar= input("Ingrese productos que se requieren comprar: ")
#"pasta pera papa coco"
lista=prod_comprar.split()

data = json.loads(prod_disponibles)

for i in lista:
  for j in data:
    if j==i:
      suma=suma+data[i]

print(suma)

for i in lista:
  for j in data:
    if j==i:
      print(j,end=" ")
