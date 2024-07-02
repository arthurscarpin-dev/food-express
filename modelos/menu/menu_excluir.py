from modelos.menu.menu import Menu
from modelos.restaurante import Restaurante

class MenuExcluir(Menu):
    def exibir_submenu():
        Menu.exibir_titulo('Excluindo um restaurante')
        nome = input('Nome do restaurante que deseja excluir: ').title().strip()
        categoria = input(f'Categoria do restaurante {nome} que deseja excluir: ').title().strip()
        dados_restaurante = Restaurante.buscar_restaurante(nome, categoria)
        if dados_restaurante is not None:
            id_restaurante = dados_restaurante[0]
            Restaurante.excluir_restaurante(id_restaurante)
            print(f'Restaurante {nome} excluído com sucesso!')
        else:
            print(f'Restaurante {nome} não cadastrado!')
        input('\nAperte ENTER para retornar ao menu principal: ')
        Menu.menu_principal()