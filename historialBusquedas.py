#historial de busqueda de prefijos
prefijos = {
  "colombia": 57,
  "peru": 51,
  "argentina": 54,
  "mexico": 52,
  "bolivia": 591,
  "chile": 56,
  "ecuador": 593
}

ingreso= " "
busqueda = dict()

print("Prefijos Internacionales")
print("----------------------------- \n")
while True:
  ingreso = input("Pais ('q':salir): ").lower()
  if ingreso == "q":
    break
    
  valor = prefijos.get(ingreso,"Pais no disponible")
  print("{}:{}".format(ingreso,valor), "\n")

  #Contador de busquedas
  print("Registro de busquedas por el pais buscado:")
  busqueda.setdefault(ingreso,0)
  busqueda[ingreso] += 1
  print("{}:{}".format(ingreso,busqueda[ingreso]))
  print("----------------------------- \n")

  print("Registro de busquedas por paises:")
  for pais,prefijo in busqueda.items():
    print("{}:{}".format(pais,prefijo))
  print("---------------------------------------------- \n")
