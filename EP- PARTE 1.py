# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:59:00 2018

@author: thive
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:09:18 2018

@author: thive
"""

#EP
Stock = {}
Option = -1

print('\nCONTROLE DE ESTOQUE ABERTO')

while Option != 0:
    print('\n0 - SAIR ')
    print('1 - ADICIONAR UM ITEM AO ESTOQUE')
    print('2 – REMOVER ITEM DO ESTOQUE')
    print('3 – ALTERAR ITEM DO ESTOQUE')
    print('4 - IMPRIMIR ESTOQUE')
    Option = int(input('Escolha um comando: '))
    
    if Option == 1:
        Product = input('Nome do produto: ')
        if Product in Stock:
            print('\nEste produto ja existe nesse estoque.')
        else:
            Quantity = int(input('Quantidade inicial: '))
            Price = float(input('Preco do produto: R$ '))
            if Price >= 0:
                Stock[Product] = {'Quantity': Quantity, 'Value': Price,\
                       'z total': Quantity*Price}
                print('\nItem adicionado com sucesso.')
            else:
                print('\nValor invalido!')
                
    elif Option == 2:
        Product = input('Nome do produto: ')
        if Product in Stock:
            del Stock[Product]
            print ('\nO item foi removido com sucesso!')
        else:
            print('\nEste produto nao foi encontrado no estoque.')
                
    elif Option == 3:
        Product = input('Nome do produto: ')
        if Product in Stock:
            Command = -1
            print('\nA atual quantidade deste produto no estoque é: {0}' .format(Stock[Product]['Quantity']))
            print('\nO preco deste produto é: R${0}'.format(Stock[Product]['Value']))
            print('\n5 - ALTERAR A QUANTIDADE DO PRODUTO')
            print('\n6 - ALTERAR O PREÇO DO PRODUTO')
            print('\n7 - ALTERAR A QUANTIDADE E O PREÇO DO PRODUTO')
            Command = int(input('\nEscolha um comando: '))
            if Command == 5:
                Quantity = (int(input('\nQuantidade a ser adicionada: ')))
                Stock[Product]['Quantity']+= Quantity
                print('\nA nova quantidade de produtos no estoque é: {0}'.format(Stock[Product]['Quantity']))
            elif Command == 6:
                New_Price = float(input('\nNovo preco do produto: R$ '))
                if New_Price >= 0:
                    Stock[Product]['Value'] = New_Price
                    print('\nO novo preco do produto é: R${0}'.format(Stock[Product]['Value']))
                else:
                    print('\nValor invalido')
                    
            elif Command == 7:
                Quantity = int(input('\nQuantidade a ser adicionada: '))
                New_Price = float(input('\nNovo preco a adicionar: R$'))
                Stock[Product]['Quantity'] += Quantity
                if New_Price >= 0:
                    Stock[Product]['Value'] = New_Price
                    print('\nA nova quantidade deste produto é: {0}'.format(Stock[Product]['Quantity']))
                    print('nO novo preco deste produto é: R${0}'.format(Stock[Product]['Value']))
                else:
                    print('\nValor invalido')
            else:
                print('O produto nao foi encontrado no estoque!')
            
    elif Option == 4:
        print('\n8 - IMPRIMIR O ESTOQUE COMPLETO')
        print('\n9 - IMPRIMIR PRODUTOS COM QUANTIDADE NEGATIVA')
        print('\n10 - IMPRIMIR O VALOR MONETÁRIO TOTAL')
        Command = int(input('\nEscolha um comando: '))
            
        
    elif Option != 0:
        print('\nComando invalido!')
            
if Option == 0:
    print('\nCONTROLE DE ESTOQUE ENCERRADO')
    print('\nATE LOGO!')
    