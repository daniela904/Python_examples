pp=int(input("valor del producto de papelería: "))
ph=2*pp+4
pl=(pp+ph)//5
print(pp, end=" ")
print (ph, end=" ")
print (pl)

#nivel generado producto de limpieza
if pl>=0 and pl<=20:
  print("uno")
elif pl>20 and pl<=30:
  print("dos")
elif pl>30 and pl<=50:
  print("tres")
else:
  print("cuatro")
