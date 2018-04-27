# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:49:24 2018

@author: thive
"""

from firebase import firebase

firebase = firebase.FirebaseApplication('https://codigo-caixa.firebaseio.com',None)
if firebase.get('Lojas',None) is None:
    Stockao = {}
else:
    Stockao = firebase.get('Lojas', None)

Medidor = 1        
Option = 1
Stock = {}
print('\nCONTROLE DE CAIXA ABERTO')
while Medidor != 0:
    print('\n*Para visualizar todas as lojas, digite "lojas"*\n'\
          '\n*Para limpar o sistema, digite "limpar"*\n'\
          '\n*Para sair do sistema, digite "sair"*')
    Loja = input('\n DIGITE UMA LOJA PARA ENTRAR OU ADICIONAR:  ')
    if Loja == 'lojas':
        if Stockao == {}:
            print('\n\nEstoque Vazio\n\n\n')

        else:
            print(Stockao)
    elif Loja == 'limpar':
        Stockao = {}
        firebase.delete('Lojas',Stockao)
        print('\nSistema limpo com sucesso\n')
    elif Loja == 'sair':
        Option = -1
        Medidor = 0
    else:
        if Loja in Stockao:
            Stock = Stockao[Loja]
        elif Loja not in Stockao:
            Stockao[Loja] = Stock
        
        while Option != -1:
            print('\n-- CONTROLE DA LOJA--\n\n'\
                  '1 - ADICIONAR UM ITEM AO ESTOQUE\n'\
                  '2 – REMOVER ITEM DO ESTOQUE\n'\
                  '3 – ALTERAR ITEM DO ESTOQUE\n'\
                  '4 - IMPRIMIR ESTOQUE\n'\
                  '5 - LIMPAR ESTOQUE DA LOJA\n'\
                  '\n-- CONTROLE DO ESTOQUE TOTAL--\n\n'\
                  '6 - TROCAR DE LOJA\n'\
                  '7 - DELETAR UMA LOJA'\
                  '8 - IMPRIMIR ESTOQUE TOTAL\n'\
                  '9 - LIMPAR TUDO\n'\
                  '\n0 - SALVAR E SAIR \n\n')
            Option = int(input('Escolha um comando: '))
            if Option == 0:
                Option = -1
                Medidor = 0
            elif Option == 1:
                Product = input('Nome do produto: ')
                if Product in Stock:
                    print('\nEste produto ja existe nesse estoque.')
                else:
                    Quantidade = int(input('Quantidade inicial: '))
                    Preço = float(input('Preco do produto: R$ '))
                    if Preço >= 0:
                        Stock[Product] = {'Quantidade': Quantidade, 'Valor': Preço,\
                               'Valor total': Quantidade*Preço}
                        Stockao[Loja] = Stock
                        print('\nItem adicionado com sucesso.')
                    else:
                        print('\nValor invalido!')
                        
            elif Option == 2:
                Product = input('Nome do produto: ')
                if Product in Stock:
                    del Stock[Product]
                    firebase.delete('Lojas/{0}'.format(Product))
                    print ('\nO item foi removido com sucesso!')
                else:
                    print('\nEste produto nao foi encontrado no estoque.')
                        
            elif Option == 3:
                Product = input('Nome do produto: ')
                if Product in Stock:
                    Command = -1
                    print('\nA atual quantidade deste produto no estoque é: {0}' .format(Stock[Product]['Quantidade']))
                    print('\nO preco deste produto é: R${0}'.format(Stock[Product]['Valor']))
                    print('\n5 - ALTERAR A QUANTIDADE DO PRODUTO')
                    print('\n6 - ALTERAR O PREÇO DO PRODUTO')
                    print('\n7 - ALTERAR A QUANTIDADE E O PREÇO DO PRODUTO')
                    Command = int(input('\nEscolha um comando: '))
                    if Command == 5:
                        Quantidade = (int(input('\nQuantidade a ser adicionada: ')))
                        Stock[Product]['Quantidade']+= Quantidade
                        print('\nA nova quantidade de produtos no estoque é: {0}'.format(Stock[Product]['Quantidade']))
                    elif Command == 6:
                        Novo_Preço = float(input('\nNovo preco do produto: R$ '))
                        if Novo_Preço >= 0:
                            Stock[Product]['Valor'] = Novo_Preço
                            print('\nO novo preco do produto é: R${0}'.format(Stock[Product]['Valor']))
                        else:
                            print('\nValor invalido')
                            
                    elif Command == 7:
                        Quantidade = int(input('\nQuantidade a ser adicionada: '))
                        Novo_Preço = float(input('\nNovo preco a adicionar: R$'))
                        Stock[Product]['Quantidade'] += Quantidade
                        if Novo_Preço >= 0:
                            Stock[Product]['Valor'] = Novo_Preço
                            print('\nA nova quantidade deste produto é: {0}'.format(Stock[Product]['Quantidade']))
                            print('nO novo preco deste produto é: R${0}'.format(Stock[Product]['Valor']))
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
                        print('{0}: Quantidade = {1}; Valor = {2}'.format(i, Stock[i]['Quantidade'], Stock[i]['Valor']))
                    if i not in Stock:
                        print('Estoque vazio')
                        
                elif Command == 9:
                    print(' ')
                    estoque_negativo = {}
                    for i in Stock:
                        if Stock[i]['Quantidade'] < 0:
                            estoque_negativo[i] = Stock[i]['Quantidade']
                            print('\n{0}: {1}'.format(i, Stock[i]['Quantidade']))
                        else:
                            print('Não existem estoques com quantidade negativa')
                        
                elif Command == 10:
                    Monetary = 0
                    for i in Stock:
                        Monetary += Stock[i]['Quantidade'] * Stock[i]['Valor']
                    print('\nO valor monetario total do seu estoque é: R${0}'.format(Monetary))
            elif Option ==5:
                LOJA = input('NOME DA LOJA: ')
                e = 0
                while e == 0:
                    print('\n1- SIM')
                    print('\n2- NÃO\n')
                    Resposta=(int(input('REALMENTE DESEJA DELETAR O ESTOQUE?:')))
                    if Resposta == 1:
                        if LOJA in Stockao:
                            Stock = {}
                            print ('\nO ESTOQUE FOI ZERADO COM SUCESSO!')
                            e = 1
                        else:
                            print('\nLOJA NÃO ENCONTRADA.')
                            e = 0
                    elif Resposta == 2:
                        print('\nLIMPEZA DE ESTOQUE CANCELADA.')
                        Option = -2
                        e = 1
                    
            elif Option == 6:
                Option = -1
                Medidor = 1
            
            elif Option == 7:
                Lojinha = input('Nome da loja: ')
                if Lojinha in Stockao:
                    del Stockao[Lojinha]
                    firebase.delete('Lojas',Lojinha)
                    print ('\nO item foi removido com sucesso!')
                else:
                    print('\nEste produto nao foi encontrado no estoque.')
                
            elif Option == 8:

                print(' ')
                if Stockao == {}:
                    print('\nEstoque vazio\n\n')
                    
                else:
                    print(Stockao)                
            
            elif Option == 9:
                a = 0
                while a == 0:
                    print("-------------------")
                    print('\n1- SIM')
                    print('\n2- NÃO\n')
                    Resposta=(int(input('REALMENTE DESEJA DELETAR TUDO?:')))
                    if Resposta == 1:
                        Stockao = {}
                        firebase.delete('Lojas',Stockao)
                        print ('\nOPERAÇÃO REALIZADA COM SUCESSO!')
                        a = 1
                    elif Resposta == 2:
                        print('\nOPERAÇÃO CANCELADA.')
                        Option = -2
                        a = 1
                    else:
                        print('\nCOMANDO INVALIDO.')
                        a = 0
                Option = -1
                Medidor = 1

            else:
                print('\nCOMANDO INVALIDO.')
            
        if Medidor == 1:
            Option = 0
Option = 0      
if Option == 0:
    print('\nCONTROLE ENCERRADO')
    print('\nATÉ A PROXIMA!')

firebase.patch("/Lojas",Stockao)