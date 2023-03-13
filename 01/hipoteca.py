# David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija nominal anual del 5%.
# Pidió $500.000 al banco y acordó un pago mensual fijo de $2684,11.
# El siguiente es un programa que calcula el monto total que pagará David a lo largo de los años:
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))



# Supongamos que David adelanta pagos extra de $1000/mes durante los primeros 12 meses de la hipoteca.
# Modificá el programa para incorporar estos pagos extra y que imprima el monto total pagado junto con la cantidad de meses requeridos.
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1

while saldo > 0:
    if mes <= 12:
        saldo = saldo * (1 + tasa / 12) - pago_mensual - 1000
        total_pagado = total_pagado + pago_mensual + 1000
        mes+=1
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


# ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años, comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    if pago_extra_mes_comienzo <= mes <= pago_extra_mes_fin:
        saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
        mes+=1
        print(f'mes {mes} - total pagado: {total_pagado} - saldo: {saldo}')
    else:
        if(mes == 310):
            total_pagado += saldo
            saldo -= saldo
            print(f'mes {mes} - pagado: {round(total_pagado, 2)} - saldo: {round(saldo, 2)}')
            mes += 1
        else:
            saldo = saldo * (1 + tasa / 12) - pago_mensual
            total_pagado = total_pagado + pago_mensual
            print(f'mes {mes} - pagado: {round(total_pagado, 2)} - saldo: {round(saldo, 2)}')
            mes += 1

print('Total pagado', round(total_pagado, 2))