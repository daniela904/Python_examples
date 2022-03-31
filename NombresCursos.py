sala1="ggt"
sala2="tdr"
nombres="ofgpbtrvuwsdnhdcmrizbutadvviy"
contA=0
contB=0
num=0

while(num<len(nombres)):
  for i in sala1:
    if nombres[num]==i:
      contA+=1
      break

  for j in sala2:
    if nombres[num]==j:
      contB+=1
      break
      
  #Bono
  if contA==contB:
    print('N',end="")
  elif contA>contB:
    print('A',end="")
  elif contA<contB:
    print('B',end="")
  
  num+=1

print(contA,contB)
