from modelos.menu.menu import Menu
from modelos.restaurante import Restaurante

class MenuAlternar(Menu):
    def exibir_submenu():
        Menu.exibir_titulo('Alternar estado de um restaurante')
        nome = input('Nome do restaurante que deseja alternar o estado: ').title().strip()
        categoria = input(f'Categoria do restaurante {nome} que deseja alternar o estado: ').title().strip()
        dados_restaurante = Restaurante.buscar_restaurante(nome, categoria)
        if dados_restaurante is not None:
            id_restaurante, estado, avaliacao = dados_restaurante
            Restaurante.alternar_status(id_restaurante, estado)
        else:
            print(f'Restaurante {nome} não cadastrado!')
        input('\nAperte ENTER para retornar ao menu principal: ')
        Menu.menu_principal()