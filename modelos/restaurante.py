import json
from modelos.banco.conexao_banco import ConexaoBanco

class Restaurante:

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False

    @staticmethod
    def _realizar_conexao():
        return ConexaoBanco()

    @classmethod
    def exibir_restaurantes(cls):
        conexao = cls._realizar_conexao()
        restaurantes = conexao.consultar_restaurantes()
        if restaurantes:
            print(f'{"Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Estado".ljust(25)} | Média Avaliação')
            for restaurante in restaurantes:
                estado = 'Desativado' if restaurante.status == False else 'Ativado'
                media = '-' if restaurante.avaliacao is None else round(float(restaurante.avaliacao), 1)
                print(f'{restaurante.nome_restaurante.ljust(25)} | {restaurante.categoria.ljust(25)} | {estado.ljust(25)} | {str(media)}')
        else:
            print("Nenhum restaurante encontrado.")

    @classmethod
    def buscar_restaurante(cls, nome, categoria):
        conexao = cls._realizar_conexao()
        restaurantes = conexao.consultar_restaurantes()
        if restaurantes:
            for restaurante in restaurantes:
                nome_restaurante = restaurante[1]
                nome_categoria = restaurante[2]
                if nome_restaurante == nome and nome_categoria == categoria:
                    id_restaurante = restaurante[0]
                    status = restaurante[3]
                    nota = restaurante[4]
                    if nota == None:
                        media = 0  
                    else:
                        media = nota
                    return id_restaurante, status, media
            return None 
        else:
            return None  

    @classmethod
    def alternar_status(cls, id, status):
        id_restaurante = id
        estado = '1' if status == False else '0'
        conexao = cls._realizar_conexao()
        conexao.atualizar_status_restaurante(id_restaurante, estado)

    @classmethod
    def avaliar_restaurante(cls, nota, id, avaliacao):
        nota_recebida = nota
        id_restaurante = id
        media_atual = avaliacao
        if 0 <= nota <= 5:
            Restaurante.calcular_media(nota_recebida, id_restaurante, media_atual)  
        else: 
            print('A nota informada é inválida.')

    @classmethod
    def calcular_media(cls, nota, id, avaliacao):
        notas = []
        nota_recebida = nota
        id_restaurante = id
        media_atual = avaliacao
        notas.append(nota_recebida)
        media_atual != 0 and notas.append(avaliacao)    
        media = (sum(notas)) / len(notas)
        conexao = cls._realizar_conexao()
        conexao.atualizar_media_restaurante(id_restaurante, media)

    @classmethod
    def excluir_restaurante(cls, id):
        id_restaurante = id
        conexao = cls._realizar_conexao()
        conexao.deletar_restaurante(id_restaurante)

    def cadastrar_restaurante(self):
        estado = '0' if not self._ativo else '1'   
        conexao = self._realizar_conexao()
        conexao.inserir_restaurante(self._nome, self._categoria, estado)