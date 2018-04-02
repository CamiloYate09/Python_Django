import string
import random

fo = open("texto.txt","wb")

fo.write("Python es lo mejor. \n es Genial \n")
for i in range(1000):
    texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    fo.write(texto)
fo.close()

fo2 = open("texto.txt","r+")
srti = fo2.read()
print( srti)
fo2.close()