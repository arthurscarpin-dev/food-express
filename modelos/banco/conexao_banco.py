import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class ConexaoBanco:
    def __init__(self):
        self._driver = os.getenv('DB_DRIVER')
        self._server = os.getenv('DB_SERVER')
        self._banco = os.getenv('DB_NAME')
        self._conexao = None

    def _conectar_ao_banco(self):
        dados_conexao = (
            f"Driver={self._driver};"
            f"Server={self._server};"
            f"Database={self._banco};"
        )
        try:
            self._conexao = pyodbc.connect(dados_conexao)
            return self._conexao
        except pyodbc.Error as ex:
            print(f'Erro de conexão: {str(ex)}')
            return None

    def inserir_restaurante(self, restaurante, categoria, estado):
        if not restaurante.strip() or not categoria.strip() or not estado.strip():
            print('Nenhum dos campos pode estar vazio.')
            return
        
        conexao = self._conectar_ao_banco()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    comando = "INSERT INTO Restaurante (nome_restaurante, categoria, status) VALUES (?, ?, ?)"
                    cursor.execute(comando, (restaurante, categoria, estado))
                    conexao.commit()
                    print(f'O restaurante {restaurante} foi cadastrado com sucesso.')
            except pyodbc.Error as ex:
                print(f'Erro ao inserir restaurante: {str(ex)}')
            finally:
                conexao.close()

    def consultar_restaurantes(self):
        conexao = self._conectar_ao_banco()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    comando = "SELECT * FROM Restaurante"
                    cursor.execute(comando)
                    linhas = cursor.fetchall()
                    return linhas
            except pyodbc.Error as ex:
                print(f'Erro ao consultar restaurantes: {str(ex)}')
                return None
            finally:
                conexao.close()

    def atualizar_status_restaurante(self, id_restaurante, estado):
        conexao = self._conectar_ao_banco()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    comando = "UPDATE Restaurante SET status = ? WHERE id_restaurante = ?"
                    cursor.execute(comando, (estado, id_restaurante))
                    conexao.commit()
                    print('O estado foi alterado com sucesso.')
            except pyodbc.Error as ex:
                print(f'Erro ao alterar o estado do restaurante: {str(ex)}')
            finally:
                conexao.close()

    def atualizar_media_restaurante(self, id_restaurante, media):
        conexao = self._conectar_ao_banco()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    comando = "UPDATE Restaurante SET avaliacao = ? WHERE id_restaurante = ?"
                    cursor.execute(comando, (media, id_restaurante))
                    conexao.commit()
                    print('Avaliação efetuada.')
            except pyodbc.Error as ex:
                print(f'Erro ao efetuar a avaliação: {str(ex)}')
            finally:
                conexao.close()

    def deletar_restaurante(self, id_restaurante):
        conexao = self._conectar_ao_banco()
        if conexao:
            try:
                with conexao.cursor() as cursor:
                    comando = "DELETE FROM Restaurante WHERE id_restaurante = ?"
                    cursor.execute(comando, (id_restaurante,))
                    conexao.commit()
                    print(f'Restaurante deletado com sucesso.')
            except pyodbc.Error as ex:
                print(f'Erro ao deletar restaurante: {str(ex)}')
            finally:
                conexao.close()
