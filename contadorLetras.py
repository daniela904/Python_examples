#contador de letras
frase = "Hola mundo, hoy es un buen dia."
conteo = dict()

#primera opcion todo en minuscula:
for i in frase.lower():
  if i not in conteo:
    conteo[i] = 1
  else:
    conteo[i] += 1

for letra, num in conteo.items():
  print("{}: {}". format(letra,num))

#segunda opcion considera mayusculas y minusculas:
for i in frase:
  conteo[i] = frase.count(i)

for letra, num in conteo.items():
  print("{}: {}". format(letra,num))
