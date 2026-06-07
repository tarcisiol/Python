import math
sen = float (input('Qual vai ser o seno?'))
cos = float (input('Qual vai ser a cosente? '))
tan = float (input('Qual vai ser a tangente? '))
sen = math.sin (math.radians(sen))
cos = math.cos (math.radians(cos))
tan = math.tan (math.radians(tan))
print (f'O seno é {sen} O coseno é {cos} A tangente é {tan}')