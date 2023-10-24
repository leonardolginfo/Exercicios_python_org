
#verifica se a entrada é menor ou igual a 140 e tweet ou mute
T = input()
E_140 = False   
LIMIT = 140

if(len(T)<=LIMIT):
  E_140 = True
if(E_140):
  print("TWEET")
else:
  print("MUTE")
  