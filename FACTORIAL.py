
# factorial = int(input("Ingresa Un numero para saber su factorial"))
#
# acum = 1
#
# while factorial>0:
#     acum *=factorial
#     factorial = factorial-1
#
#
#
# print('%i' % acum)


#FACTORIAL DE FORMA RECURSIVA

def factorial(x):
    if (x==0):
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))