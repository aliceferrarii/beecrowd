start_hora = int(input('hora inicio: '))
start_minuto = int(input('minuto inicio: '))
end_hora = int(input('hora termino: '))
end_minuto = int(input('minuto termino: '))

duracao_hora = end_hora - start_hora
duracao_minuto = end_minuto - start_minuto

print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)")

