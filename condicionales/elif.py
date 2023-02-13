ingreso_mensual = 10000
gasto_mensual = 4000

if ingreso_mensual > 8000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual >= 5000 :
        print("estas manejando bien la plata")
    else :
        print("estas gastando mucha plata")

