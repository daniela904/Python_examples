'''Programa que sirve para repasar las capitales de algunos paises. Cumple con los siguientes requisitos:

- Se pregunta por la capital de los paises en orden aleatorio.
- Si se falla se muestra la capital del pais para aprenderla.
- Los dos requisitos anteriores se repiten hasta que se acierten todas las capitales.
- Al final del repaso vuelven a salir los paises que se han fallado.'''

import random

capitales = {
  "Canadá":"Ottawa",
  "Uruguay":"Montevideo",
  "Kenia":"Nairobi",
  "Islandia":"Reikiavik",
  "Filipinas":"Manila"
}

cont = 0
fallos = []
listaPaises = list(capitales.keys())

print("---REPASO DE CAPITALES!---")
while True:
  if len(listaPaises) != 0:
    random.shuffle(listaPaises)
    pais = random.choice(listaPaises)
    capital = input("Cual es la capital de {}: ".format(pais))
    
    if capital==capitales[pais]:
      print("CORRECTO!! Has acertado.")
      listaPaises.remove(pais)
      print("\n")
        
    else:
      print("INCORRECTO...")
      if pais not in fallos:
        fallos.append(pais) 
      print("La capital de {} es {}.".format(pais,capitales[pais]))
      print("\n")

  else:
      print("--- Te has aprendido las capitales ¡Muy bien! ---")
      if len(fallos)>0:
        print("Recuerda los paises en que fallaste y sus capitales:")
        for i in fallos:
          print("País:", i,"-", "Capital:", capitales[i], end="\n")
      break
