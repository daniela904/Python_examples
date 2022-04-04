def dayOfYear(año, mes, dia):
    if año % 4 != 0:
      print("Año no bisiesto")
      dia_año=0
      if mes==1:
        dia_año=31-(31-dia)
      elif mes > 1:
        dia_año+=31
      if mes == 2:
        dia_año=dia_año+28-(28-dia)
      elif mes > 2:
        dia_año+=28
      if mes == 3:
        dia_año=dia_año+31-(31-dia)
      elif mes >3:
        dia_año+=31
      if mes == 4:
        dia_año=dia_año+30-(30-dia)
      elif mes>4:
        dia_año+=30
      if mes == 5:
        dia_año=dia_año+30-(30-dia)
      elif mes>5:
        dia_año+=31
      if mes == 6:
        dia_año=dia_año+30-(30-dia)
      elif mes > 6:
        dia_año+=30
      if mes == 7:
        dia_año=dia_año+31-(31-dia)
      elif mes > 7:
        dia_año+=31
      if mes == 8:
        dia_año=dia_año+31-(31-dia)
      elif mes > 8:
          dia_año+=31
      if mes==9:
        dia_año=dia_año+31-(31-dia)
      elif mes > 9:
          dia_año+=30
      if mes==10:
        dia_año=dia_año+31-(31-dia)
      elif mes > 10:
          dia_año+=31
      if mes==11:
        dia_año=dia_año+30-(30-dia)
      if mes > 11:
           dia_año+=30
      if mes == 12:
          dia_año+=(31+(31-dia))
      return dia_año
      
    elif año % 4 == 0 and año % 100 != 0: 
      dia_año=0
      
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
      dia_año=0
      
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
      dia_año=0
      
print("día del año:", dayOfYear(2022, 4, 4)) #dia 94
