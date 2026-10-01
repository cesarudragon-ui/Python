PRECIO_HABITUAL = 3.49
DESCUENTO_PORCENTAJE = 60
DESCUENTO_FACTOR = 1 - (DESCUENTO_PORCENTAJE / 100)

precio_con_descuento = PRECIO_HABITUAL * DESCUENTO_FACTOR

barras_no_frescas = int(input( "Introduce el número de barras vendidas que no son del día: " ))

coste_total = barras_no_frescas * precio_con_descuento

print("--- Resumen de la venta ---")
print(f"Precio habitual de una barra: {PRECIO_HABITUAL:.2f} €")
print(f"Descuento aplicado: {DESCUENTO_PORCENTAJE}%")
print( f"Cantidad de barras no frescas vendidas: {barras_no_frescas}")

print(f"Coste final total: {coste_total:.2f} €")