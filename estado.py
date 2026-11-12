
import database as db


class Estado:


    def __init__(self):
        self.id = 0
        self.nome = ""
        self.sigla = ""


        self.db.ConexaoMySQL()


        def salvar(self):
            conn = self.db.abrir()
            if conn:
                try:
                    with conn.cursor() as cursor:
                        sql = "INSERT INTO estado (nome, sigla) VALUES (%s, %s);"
                        cursor.execute(sql, (self.nome, self.sigla))
                        conn.commit()
                        self.id = cursor.lastrowid
                        print("Salvo com sucesso!")
                except Exception as e:
                    print(f"Erro ao salvar estado: {e}")
                finally:
                    self.db.fechar()


    def listar(self):
        conn  = self.db.abrir()
        estados = []
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT id,nome,sigla FROM estado;"
                    cursor.execute(sql)
                    estados = cursor.fetchall()
            except Exception as e:
                print(f"Erro ao listar estados: {e}")
            finally:
                self.db.fechar()
        return estados


    def atualizar(self):
        conn = self.db.abrir()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "UPDATE estado SET nome = %s, sigla = %s WHERE id = %s;"
                    cursor.execute(sql, (self.nome, self.sigla, self.id))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Atualizado com sucesso!")
                    else:
                        print("Nenhum estado encontrado com o ID informado.")
            except Exception as e:
                print(f"Erro ao atualizar estado: {e}")
            finally:
                self.db.fechar()


    def excluir(self):
        conn = self.db.abrir()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM estado WHERE id = %s;"
                    cursor.execute(sql, (self.id,))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Excluído com sucesso!")
                    else:
                        print("Nenhum estado encontrado com o ID informado.")
            except Exception as e:
                print(f"Erro ao excluir estado: {e}")
            finally:
                self.db.fechar()
