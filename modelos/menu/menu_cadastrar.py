from modelos.menu.menu import Menu
from modelos.restaurante import Restaurante

class MenuCadastrar(Menu):
    def exibir_submenu():
        Menu.exibir_titulo('cadastre um restaurante')
        restaurante = input('Nome do restaurante que deseja cadastrar: ').title().strip()
        categoria = input(f'Nome da categoria do {restaurante}: ').title().strip()
        dados_restaurante = Restaurante(restaurante, categoria)
        nome = dados_restaurante._nome
        categoria = dados_restaurante._categoria
        restaurante_retornado = dados_restaurante.buscar_restaurante(nome, categoria)
        dados_restaurante.cadastrar_restaurante() if restaurante_retornado is None else print(f'Restaurante {dados_restaurante._nome} já cadastrado!')
        input('\nAperte ENTER para retornar ao menu principal: ')
        Menu.menu_principal()