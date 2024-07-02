from modelos.menu.menu import Menu
from modelos.restaurante import Restaurante

class MenuAvaliar(Menu):
    def exibir_submenu():
        Menu.exibir_titulo('Avalie um restaurante')
        nome = input('Nome do restaurante que deseja avaliar: ').title().strip()
        categoria = input(f'Categoria do restaurante {nome} que deseja avaliar: ').title().strip()
        dados_restaurante = Restaurante.buscar_restaurante(nome, categoria)
        if dados_restaurante is not None:
            status = dados_restaurante[1]
            if status != False:
                nota = float(input('Informe uma nota entre 0 e 5: ').strip())
                id_restaurante = dados_restaurante[0]
                media_atual = dados_restaurante[2]
                Restaurante.avaliar_restaurante(nota, id_restaurante, media_atual)
            else:
                print('Restaurante desativado!')
        else:
            print(f'Restaurante {nome} não cadastrado!')
        input('\nAperte ENTER para retornar ao menu principal: ')
        Menu.menu_principal()