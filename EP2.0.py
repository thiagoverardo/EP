# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 08:09:18 2018

@author: thive
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:42:23 2018

@author: thiagoverardo
"""
#EP

import json
import os

jason = open('estoque.json','r')
jason.close()

with open('estoque.json','r') as arquivo:
    if os.stat('estoque.json').st_size == 0:
        Stock = {}
    else:
        conteudo = arquivo.read()
        Stock = json.loads(conteudo)
        
Option = -1

print('\nCONTROLE DE ESTOQUE ABERTO')

while Option != 0:
    print('\n0 - sair ')
    print('1 - adicionar item ')
    print('2 - remover item ')
    print('3 - alterar item ')
    print('4 - imprimir estoque ')
    Option = int(input('Escolha um comando: '))
    
    if Option == 1:
        produto = input('Nome do produto: ')
        if produto in Stock:
            print('\nEste produto ja existe nesse estoque.')
        else:
            quantidade = int(input('Quantidade inicial: '))
            preco = float(input('Preco do produto: R$ '))
            if preco >= 0:
                Stock[produto] = {'quantidade': quantidade, 'valor': preco,\
                       'z total': quantidade*preco}
                print('\nItem adicionado com sucesso.')
            else:
                print('\nValor invalido!')
                
    elif Option == 2:
        produto = input('Nome do produto: ')
        if produto in Stock:
            del Stock[produto]
            print ('\nO item foi removido com sucesso!')
        else:
            print('\nEste produto nao foi encontrado no estoque.')
                
    elif Option == 3:
        produto = input('Nome do produto: ')
        if produto in Stock:
            comando = -1
            print('\nA atual quantidade deste produto no estoque eh: {0}' .format(Stock[produto]['quantidade']))
            print('\nO preco deste produto eh: R${0}'.format(Stock[produto]['valor']))
            print('\n5 - alterar a quantidade do produto no estoque')
            print('\n6 - alterar o preco do produto')
            print('\n7 - Alterar a quantidade do produto')
            comando = int(input('\nEscolha um comando: '))
            if comando == 5:
                quantidade = (int(input('\nQuantidade a ser adicionada: ')))
                Stock[produto]['quantidade']+= quantidade
                print('\nA nova quantidade de produtos no estoque eh: {0}'.format(Stock[produto]['quantidade']))
            elif comando == 6:
                novo_preco = float(input('\nNovo preco do produto: R$ '))
                if novo_preco >= 0:
                    Stock[produto]['valor'] = novo_preco
                    print('\nO novo preco do produto eh: R${0}'.format(Stock[produto]['valor']))
                else:
                    print('\nValor invalido')
                    
            elif comando == 7:
                quantidade = int(input('\nQuantidade a ser adicionada: '))
                novo_preco = float(input('\nNovo preco a adicionar: R$'))
                Stock[produto]['quantidade'] += quantidade
                if novo_preco >= 0:
                    Stock[produto]['valor'] = novo_preco
                    print('\nA nova quantidade deste produto eh: {0}'.format(Stock[produto]['quantidade']))
                    print('nO novo preco deste produto eh: R${0}'.format(Stock[produto]['valor']))
                else:
                    print('\nValor invalido')
            else:
                print('O produto nao foi encontrado no estoque!')
            
    elif Option == 4:
        print('\n8 - Imprimir o estoque completo')
        print('\n9 - Listar produtos com quantidade negativa')
        print('\n10 - Exibir um valor monetario total')
        comando = int(input('\nEscolha um comando: '))
            
        if comando == 8:
            print(' ')
            for i in Stock:
                print('{0}: quantidade = {1}; valor = {2}'.format(i, Stock[i]['quantidade'], Stock[i]['valor']))
            if i not in Stock:
                print('Estoque vazio')
                
        elif comando == 9:
            estoque_negativo = {}
            for i in Stock:
                if Stock[i]['quantidade'] < 0:
                    estoque_negativo[i] = Stock[i]['quantidade']
                    print('\n{0}: {1}'.format(i, Stock[i]['quantidade']))
                
        elif comando == 10:
            monetario = 0
            for i in Stock:
                monetario += Stock[i]['quantidade'] * Stock[i]['valor']
            print('\nO valor monetario total do seu estoque eh: R${0}'.format(monetario))
                
    elif Option != 0:
        print('\nComando invalido!')
            
if Option == 0:
    print('\nCONTROLE DE ESTOQUE ENCERRADO')
    print('\nATE LOGO!')
    novo_estoque = json.dumps(Stock, sort_keys = True, indent = 0)
    with open('estoque.json', 'w') as f:
        novo_conteudo = f.write(novo_estoque)
