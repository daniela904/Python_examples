cont=0
suma=0
prod = input("Inserte los productos: ")

prod_lista=prod.split()
print(prod_lista)

#lista de elementos sin elementos que se repiten seguido
print(prod_lista[0],end=" ")
while cont<len(prod_lista):
  if cont>=1:
    if prod_lista[cont]==prod_lista[cont-1]:
      prod_repetido=prod_lista[cont-1]
    else:
      prod_repetido=prod_lista[cont]

    if prod_repetido!=prod_lista[cont-1]:
      print(prod_lista[cont],end=" ")
  cont+=1
print("\n")

#contador de elementos repetidos seguidos
cont=0
while cont<len(prod_lista):
  suma=1
  if cont==len(prod_lista)-1:
    print(end=" ")
  else:
    while prod_lista[cont]==prod_lista[cont+1]:
      cont+=1
      suma+=1
      if cont==len(prod_lista)-1:
        break
  print(suma, end=" ")
  cont+=1
