#ingresos y gastos diarios
ingreso_diario = 100000
gasto_gasolina_diario = 10000

#gastos mensuales fijos
gasto_internet_mensual = 80000
gasto_casa_mensual = 200000
cuota_moto_mensual = 300000
pago_tarjetacredito_mensual = 100000

#ingreso y gasto mensual fijos
ingreso_mensual = 1600000
gasto_mensual_total = gasto_internet_mensual + gasto_casa_mensual + cuota_moto_mensual + pago_tarjetacredito_mensual

#dinero disponible mensual y diario
dinero_disponible_diario = ingreso_diario - gasto_gasolina_diario
dinero_disponible_final_mes = ingreso_mensual - gasto_mensual_total

print ("El ingreso diario de Manuel es:", ingreso_diario)
print ("El gasto diario de Manuel es:", gasto_gasolina_diario)
print ("El ingreso mensual de Manuel es:", ingreso_mensual)
print ("El gasto_mensual_total de Manuel es:", gasto_mensual_total)

compra_mensual = 800000
compra_diaria = 120000

if compra_mensual <= dinero_disponible_final_mes:
    print("Puedes hacer la compra del MES")
else:
    print("No puedes hacer la compra, ¡AHORRA para el próximo mes!")

if gasto_gasolina_diario >= dinero_disponible_diario:
    print("No puedes hacer la compra de hoy")
else:
    print("SI!, haz la compra")


    