#and
#para que devuelva true debe haber dos true si hay uno falso el resultado va a ser falso

resultado = True & True #devolver true 
resultado_2 = False & True #devolver falso
resultado_3 = True & False #devolvere falso 
resultado_4 = False & False #devolver falso

#or
#or devuelve falso solo cuando las dos condiciones son falsas
resultado_5 = True | True #devolver true
resultado_6 = False | True #devolver true
resultado_7 = True | False #devolver true
resultado_8 = False | False #devolver falso

#not
#si es not true devuelve falso y sies not false devuelve true 
resultado_9 = not True #devolver falso
resultado_10 = not False #devolver true

print(resultado_10)