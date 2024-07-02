import time
from modelos.menu.menu import Menu

class MenuEncerrar(Menu):
    def exibir_submenu():
        print('A aplicação está sendo encerrada...')
        time.sleep(5)
        Menu.limpar_console()
        print('Tchau Tchau :)') 