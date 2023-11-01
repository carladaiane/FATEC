
""" Uma pessoa muito organizada gostaria de fazer um algoritmo para armazenar os
seguintes dados de um talonário após a utilização total do mesmo: n2do cheque,
valor, data e destino. Sabendo-se que o número de cheques pode ser variável e
não ultrapassa 20, construa esse algoritmo de tal maneira que possa gerar um relatório no vídeo. """


banco = []

""" nome = input('\n Digite o número do cheque: ')

idade = input('\n Digite o valor do cheque: ') """

""" input('\n Digite a data do cheque: ')

input('\n Digite o destinodo cheque: ')
 """


while len(banco)<=3:
    nome = input('\n Digite o número do cheque: ')
    idade = input('\n Digite o valor do cheque: ')
    banco.append({"nome":nome, "idade":idade})

    if len(banco)==3:
        break



print(banco)





""" prog vetor13
string num[20], valor[20], destino[20], data[20], resp;
int nc, k;
imprima "\nnumero de cheques do talonario:
leia nc;
para( k <- O; k < nc; k++)
{ imprima "\nnumero do cheque:
leia num[k];
imprima "\nvaor do cheque:
leia valor[k];
imprima "\ndata do cheque ddmmaa:
leia data[k];
imprima "\ndestino do cheque:
leia destino[k];
}
imprima "\nRELACAO dos CHEQUES\n";
para( k <-O; k < nc; k++)
{ imprima "\nNumero do cheque: ', num[k];
imprima "\nValor do cheque: ", valor[k];
imprima "\nData do cheque: ", data[k];
imprima "\nDestino do cheque: ", num[k];
imprima "\n\nPressione enter para ver outro cheque:
leia resp; # necessario pois a tela so tem 25 linhas
}
imprima "\n";
fimprog  """