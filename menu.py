# Faz a importação das bibliotecas e funções
import os
from time import sleep

# Cria a função firula() que serve como estilizador do programa
def firula(msg):
    print("by JeanOmeg")
    print("=" * 70, "\n")
    print(msg, "\n")
    print("=" * 70, "\n")
    
    
# Abertura do loop raíz do menu pricipal
menuprincipal = '0'
while menuprincipal == '0':
    os.system('clear')
    firula("OPÇÕES DO MENU")
    menu = input('[1]MENU-1  [2]MENU-2  [3]SAIR: ')
    
# Abertura do menu-1
    if menu == '1':
        sleep(1)
        os.system('clear')
        firula('[1]MENU-1 SELECIONADO')
        sleep(1)
        print('EXECUTA ALGUMA COISA')
        sleep(2)
        os.system('clear')
        firula('ACESSAR MENU PRINCIPAL OU SAIR DO PROGRAMA?')
        submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        while submenu.lower() != '1' and submenu.lower() != '2':
            sleep(2)
            os.system('clear')
            firula('OPÇÃO INVÁLIDA')
            submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        else:
            if submenu.lower() == '1':
                sleep(2)
                os.system('clear')
                firula('ACESSANDO MENU PRINCIPAL')
                sleep(2)
                menuprincipal = '0'
            else:
                sleep(2)
                os.system('clear')
                firula('FECHANDO PROGRAMA')
                menuprincipal = '1'
            
# Abertura do menu-2
    elif menu == '2':
        sleep(1)
        os.system('clear')
        firula('[1]MENU-2 SELECIONADO')
        sleep(1)
        print('EXECUTA ALGUMA COISA')
        sleep(2)
        os.system('clear')
        firula('ACESSAR MENU PRINCIPAL OU SAIR DO PROGRAMA?')
        submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        while submenu.lower() != '1' and submenu.lower() != '2':
            sleep(2)
            os.system('clear')
            firula('OPÇÃO INVÁLIDA')
            submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        else:
            if submenu.lower() == '1':
                sleep(2)
                os.system('clear')
                firula('ACESSANDO MENU PRINCIPAL')
                sleep(2)
                menuprincipal = '0'
            else:
                sleep(2)
                os.system('clear')
                firula('FECHANDO PROGRAMA')
                menuprincipal = '1'
            
# Abertura do menu de saída
    elif menu == '3':
        sleep(2)
        os.system('clear')
        firula('FECHANDO PROGRAMA')
        break
        
# Abertura da exceção em caso de escolha inválida
    else:
        sleep(2)
        os.system('clear')
        firula('OPÇÃO INVÁLIDA')
        sleep(2)

# Finalização do programa
sleep(2)
os.system('clear')
firula('PROGRAMA FINALIZADO')
