Cantidad = float(input('Digame cantidad de dinero'))
Interes = float(input('Interes anual'))
Años = float(input('Cantidad de años en inversión'))
CapitalTotal = round(Cantidad * (1+(Interes/100))**Años,2)

print (f'el capital total obtenido en su imbersion es {CapitalTotal}')
