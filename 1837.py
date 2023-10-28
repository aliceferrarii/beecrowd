
def calcula_quociente_e_resto(a, b):
    q = a // b  # Calcula o quociente
    r = a % b   # Calcula o resto
    
    return q, r

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

quociente, resto = calcula_quociente_e_resto(a, b)

print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
