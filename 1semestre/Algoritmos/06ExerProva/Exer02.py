salarioFixo = float(input('Digite o valor do salário fixo: '))

valorVendas = float(input('Digite o vlaor das vendas: '))


if valorVendas <= 1500:
    comissao3 = valorVendas*0.03
    print(f'Salário:{salarioFixo} | Valor das vendas {valorVendas} | Comissão: {comissao3} | Total: {salarioFixo+comissao3}')
elif valorVendas >1500:
    sobra = (valorVendas-1500)*0.10
    print(f'Salário:{salarioFixo} | Valor das vendas {valorVendas} | Comissão: {1500*0.03+sobra} | Total: {salarioFixo+1500*0.03+sobra}')




