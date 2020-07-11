import sys    #Importando a bliblioteca sys
import math   #Importando a biblioteca math
# ax2 + bx + c
# b-4*a*c = delta 
# -b+raiz de delta/2*a valor de X
# -b-raiz de delta/2*a valor de Y

a = int(input("Digite um valor: "))

if a == 0:
    print("Não é uma equação do segundo grau")
    sys.exit(0)
else:
    b = int(input("Digite um valor: "))
    c = int(input("Digite um valor: "))
    delta = b-(4*a*c)
    if delta < 0:
        print("A equação não tem raízes")
        sys.exit(0)
    elif delta == 0:
        raiz = math.pow(delta, 1/2) 
        resultado = ((-b)+raiz)/(2*a)
        print("Os valores de X e Y são iguais, o valor deles é: {}".format(resultado))
    else:
        raiz = math.pow(delta, 1/2) 
        resultado = ((-b)+raiz)/(2*a)
        resultado2 = ((-b)-raiz)/(2*a)
    print("Os valores de X e Y são diferentes, o valor de X é {}\n o valor de Y é {}".format(resultado, resultado2))
