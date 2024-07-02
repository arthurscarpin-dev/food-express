from modelos.menu.menu import Menu
from modelos.restaurante import Restaurante

class MenuListar(Menu):
    def exibir_submenu():
        Menu.exibir_titulo('Listando todos os restaurantes')
        Restaurante.exibir_restaurantes()
        input('\nAperte ENTER para retornar ao menu principal: ').strip()
        Menu.menu_principal()