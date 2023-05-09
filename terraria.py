minerales = {
'meteorito':'Meteorito',
'carmesi':'Mineral carmesí',
'adamantita':'Mineral de adamantita',
'clorofita':'Mineral de clorofita',
'cobalto':'Mineral de cobalto',
'cobre':'Mineral de cobre',
'estaño':'Mineral de estaño',
'hierro':'Mineral de hierro',
'mithril':'Mineral de mithril',
'oricalco':'Mineral de oricalco',
'oro':'Mineral de oro',
'paladio':'Mineral de paladio',
'plata':'Mineral de plata',
'platino':'Mineral de platino',
'plomo':'Mineral de plomo',
'titanio':'Mineral de titanio',
'tugsteno':'Mineral de tungsteno',
'endemoniado':'Mineral endemoniado',
'piedra infernal':'mineral de piedra infernal',
'piñonita':'mineral de piñonita'

}
for mine in minerales:
    print(mine)

def miner():
    Time = input('que mineral quieres calcular: ')
    cantidad_de_minerales = float(input('cantidad de minerales'))
    cantidad = int(cantidad_de_minerales / 3)
    print(str(cantidad) + 'lingotes de ' + Time)

print('terrawel v.0.1 (alpha)')
print('abvertencia: esto solo finciona para aquellos lingotes que requieran de 3 minerales para ser findidos.')
pregunta = input('deseas continuar S/N')
if pregunta == 'S':
    miner()
elif pregunta == 'N':
    print('proximamente se actualizara este programa')





