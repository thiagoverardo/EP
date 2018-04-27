# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:28:59 2018

@author: thive
"""

import json
import os

jason = open('estoque.json','r')
jason.close()

with open('estoque.json','r') as Archive:
    if os.stat('estoque.json').st_size == 0:
        Stockao = {}
    else:
        Content = Archive.read()
        Stockao = json.loads(Content)
Medidor = 1        
Option = 1
Stock = {}
Stockao = {}
print('\nCONTROLE DE ESTOQUE ABERTO')
while Medidor != 0:
    Loja = input('QUAL A SUA LOJA?  ')
    if Loja in Stockao:
        Stock = Stockao[Loja]
    elif Loja not in Stockao:
        Stockao[Loja] = Stock
    
    while Option != -1:
        print('\n0 - SAIR ')
        print('1 - ADICIONAR UM ITEM AO ESTOQUE')
        print('2 – REMOVER ITEM DO ESTOQUE')
        print('3 – ALTERAR ITEM DO ESTOQUE')
        print('4 - IMPRIMIR ESTOQUE')
        print('5 - TROCAR DE LOJA')
        Option = int(input('Escolha um comando: '))
        if Option == 0:
            Option = -1
            Medidor = 0
        elif Option == 1:
            Product = input('Nome do produto: ')
            if Product in Stock:
                print('\nEste produto ja existe nesse estoque.')
            else:
                Quantity = int(input('Quantidade inicial: '))
                Price = float(input('Preco do produto: R$ '))
                if Price >= 0:
                    Stock[Product] = {'Quantity': Quantity, 'Value': Price,\
                           'Total value': Quantity*Price}
                    Stockao[Loja] = Stock
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
                
            if Command == 8:
                print(' ')
                for i in Stock:
                    print('{0}: Quantity = {1}; Value = {2}'.format(i, Stock[i]['Quantity'], Stock[i]['Value']))
                if i not in Stock:
                    print('Estoque vazio')
                    
            elif Command == 9:
                print(' ')
                estoque_negativo = {}
                for i in Stock:
                    if Stock[i]['Quantity'] < 0:
                        estoque_negativo[i] = Stock[i]['Quantity']
                        print('\n{0}: {1}'.format(i, Stock[i]['Quantity']))
                    else:
                        print('Não existem estoques com quantidade negativa')
                    
            elif Command == 10:
                Monetary = 0
                for i in Stock:
                    Monetary += Stock[i]['Quantity'] * Stock[i]['Value']
                print('\nO valor monetario total do seu estoque é: R${0}'.format(Monetary))
                
        elif Option == 5:
            Option = -1
            Medidor = 1
        else:
            print('\nComando invalido!')
        
    if Medidor == 1:
        Option = 0
Option = 0      
if Option == 0:
    print('\nCONTROLE DE ESTOQUE ENCERRADO')
    print('\nATE LOGO!')
    New_Stock = json.dumps(Stockao, sort_keys = True, indent = 0)
    with open('estoque.json', 'w') as f:
        New_Content = f.write(New_Stock)