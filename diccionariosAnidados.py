agenda = {
  "Jorge":{
    "Telefono": 1234,
    "Pais": "Colombia",
    "Personal": {
      "Deporte":"Futbol",
      "Aficion":"Leer",
      "Musica":"Clasica"
    }
  }, 
  "Maria":{
    "Telefono": 6542,
    "Pais": "Colombia",
    "Personal": {
      "Deporte":"Natacion",
      "Aficion":"Astronomia",
      "Musica":"Rock"
    }
  }, 
  "Tomas":{
    "Telefono": 9512,
    "Pais": "Mexico",
    "Personal": {
      "Deporte":"Voleyball",
      "Aficion":"Cine",
      "Musica":"Pop"
    }
  }, 
  "Carla":{
    "Telefono": 4578,
    "Pais": "Argentina",
    "Personal": {
      "Deporte":"Karate",
      "Aficion":"Ajedrez",
      "Musica":"Metal"
    }
  }
}

#extraer el nombre de la persona que sea de colombia y le guste el rock
for i in agenda.keys():
  if agenda[i]["Pais"]=="Colombia":
    if agenda[i]["Personal"]["Musica"]=="Rock":
      print(i)

#mostrar todos los miembros con su aficion
for i in agenda.keys():
  print("{}: {}".format(i,agenda[i]["Personal"]["Aficion"]))

#mostrar todos los datos personales de cada miembro
for nombre,datos in agenda.items():
  print("Los datos personales de {}".format(nombre),"son:")
  for categoria,dato in datos["Personal"].items():
    print("{}: {}".format(categoria,dato))
  print("\n")
