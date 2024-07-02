import os
from abc import ABC, abstractmethod

class Menu(ABC):

    @staticmethod
    def menu_principal():
        Menu.exibir_titulo('Food Express')
        Menu.exibir_opcoes()
        Menu.escolher_opcao()
    
    @staticmethod
    def exibir_titulo(texto):
        Menu.limpar_console()
        linha = '*' * len(texto)
        titulo = texto.upper()
        print(linha)
        print(titulo)
        print(linha, '\n')

    @staticmethod
    def limpar_console():
        os.system('cls')

    @staticmethod
    def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Exibir restaurantes.')
        print('3. Alternar o estado do restaurante.')
        print('4. Avaliar restaurante.')
        print('5. Excluir restaurante.')
        print('-1. Sair.\n')

    @staticmethod
    def escolher_opcao():
        try:
            opcao = int(input('Escolha uma opção: '))
            match opcao:
                case 1:
                    Menu._executar_submenu('menu_cadastrar', 'MenuCadastrar')
                case 2:
                    Menu._executar_submenu('menu_listar', 'MenuListar')
                case 3:
                    Menu._executar_submenu('menu_alternar', 'MenuAlternar')
                case 4:
                    Menu._executar_submenu('menu_avaliar', 'MenuAvaliar')
                case 5:
                    Menu._executar_submenu('menu_excluir', 'MenuExcluir')
                case -1:
                    Menu._executar_submenu('menu_encerrar', 'MenuEncerrar')
                case _:
                    Menu._opcao_incorreta()
        except ValueError:
            Menu._opcao_incorreta()

    @staticmethod
    def _executar_submenu(modulo, classe):
        submenu = __import__(f'modelos.menu.{modulo}', fromlist=[classe])
        getattr(submenu, classe).exibir_submenu()

    @staticmethod
    def _opcao_incorreta():
        Menu.limpar_console()
        print('Opção incorreta!')
        input('\nAperte ENTER para retornar ao menu principal: ')
        Menu.menu_principal()

    @abstractmethod
    def exibir_submenu():
        pass
