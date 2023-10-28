# N = diferença entre valores das moedas
# M = quantidade de moedas
# Vi = valores da moeda Mi 
# soma valores = número primo

def verificar_jogo(m, quantidade, n):
    soma = sum(quantidade[i] for i in range(0, m, n))
    
    def is_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1): #ver se ele é primo ao dividir tambem pela raiz quadrada
            if num % i == 0:
                return False
        return True

    if is_primo(soma):
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I’ll hit you.")

def jogo():
    m = int(input('Insira a quantidade de moedas entre 2 e 20: '))
    if not (2 <= m <= 20):
        print('Por favor, insira um número entre 2 e 20.')
        return

    quantidade = []
    for i in range(m):
        v = int(input(f'Insira o valor da moeda {i+1} entre 1 e 500: '))
        if not (1 <= v <= 500):
            print('Por favor, insira valores entre 1 e 500.')
            return
        quantidade.append(v)

    n = int(input(f'Insira o salto entre as moedas (1 a {m}): '))
    if not (1 <= n <= m):
        print(f'Por favor, insira um valor entre 1 e {m}.')
        return

    verificar_jogo(m, quantidade, n)

jogo()
