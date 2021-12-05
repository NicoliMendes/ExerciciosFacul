def recebeTempo():

   i = 1

   lista = []

   while i > 0:

       i = int(input())

       if i > 0:

           lista.append(i)

       else:

           break

   return lista

def calculaMedia (lista):

   tempo = 0

   media = 0

   for tempo in range(len(lista)):

       media = media+lista[tempo]

   media = media/len(lista)

   return media

def abaixoMedia (lista, media):

   abaixo_media = []

   x = 0

   for x in range(len(lista)):

       if lista[x] < media:

           abaixo_media.append(lista[x])

   return abaixo_media

lista = recebeTempo()

media = calculaMedia(lista)

menores = abaixoMedia(lista, media)

print (f'MEDIA:{media:.2f}')

for i in range (len(menores)):

   print (f'{menores[i]}')