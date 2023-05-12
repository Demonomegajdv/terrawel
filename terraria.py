def pre_hardmode():
    cantidad = int(input('cantidad de minerales:'))
    calculo = cantidad / 3
    print(calculo)

def hardmode():
    cantidad = int(input('cantidad de minerales:'))
    calculo = cantidad / 4
    print(calculo)

print('terrawel 0.4 (alpha)')
pregunta = input('pre-hardmode o hardmode')
if pregunta == 'pre-hardmode':
    pre_hardmode()
elif pregunta == 'hardmode':
    hardmode()        