#historial de busqueda de prefijos
prefijo = {
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
  if ingreso == "q" or ingreso=="Q":
    break
    
  valor = prefijo.get(ingreso,"Pais no disponible")
  print("{}:{}".format(ingreso,valor), "\n")

  #Contador de busquedas
  print("Registro de busquedas")
  busqueda.setdefault(ingreso,0)
  busqueda[ingreso] += 1
  print("{}:{}".format(ingreso,busqueda[ingreso]))
  print("----------------------------- \n")
