Payasos = 0.112
Muneca = 0.075

CPayasos = float(input('Digame la cantidad de payasos vendidos'))
CMunecas = float(input('Digame la cantidad de muñecas vendidas'))

PesoPedido = (CPayasos * Payasos)+(CMunecas * Muneca)

print(f'El peso total de las muñecas es {PesoPedido} KG')