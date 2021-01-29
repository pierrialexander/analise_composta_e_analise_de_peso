
princ = []
temp = []
maiorpeso = menorpeso = 0
while True:
    temp.append(str(input('Qual é o seu nome: ')))
    temp.append(float(input('Qual é o seu peso? ')))
    if len(princ) == 0:
        maiorpeso = menorpeso = temp[1]
    else:
        if temp[1] > maiorpeso:
            maiorpeso = temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/n] '))
    if resp in 'Nn':
        break


print(f'Ao todo foram cadastradas {len(princ)} pessoas.')

print(f'O maior peso foi {maiorpeso}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorpeso}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
