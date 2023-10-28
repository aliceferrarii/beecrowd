def horas():
    h1 = int(input('insira a hora atual (entre 0 e 23): '))
    if not (0 <= h1 <= 23):
        print('Por favor, insira um valor entre 0 e 23')
        return
    m1 = int(input('insira o minuto atual (entre 0 e 59): '))
    if not (0 <= m1 <= 59):
        print('Por favor, insira um valor entre 0 e 59')
        return
    h2 = int(input('insira a hora do alarme (entre 0 e 23): '))
    if not (0 <= h2 <= 23):
        print('Por favor, insira um valor entre 0 e 23')
        return   
    m2 = int(input('insira o minuto do alarme (entre 0 e 59): '))
    if not (0 <= m2 <= 59):
        print('Por favor, insira um valor entre 0 e 59')
        return

    return h1, m1, h2, m2

def calculo(h1, m1, h2, m2):
    minutos_dormir = ((h2 * 60 + m2) - (h1 * 60 + m1)) % 1440
    return minutos_dormir

while True:
    h1, m1, h2, m2 = horas()
    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break
    else:
        resultado = calculo(h1, m1, h2, m2)
        print(f'Você tem {resultado} minutos de sono')
