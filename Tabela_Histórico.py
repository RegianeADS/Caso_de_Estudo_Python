import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "9513", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados realizada com sucesso!")
cur=conn.cursor()
cur.execute('''CREATE TABLE RECRIA (BRINCO INT PRIMARY KEY NOT NULL, SEXO TEXT NOT NULL, PESO REAL NOT NULL); ''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()

from faker import Faker
import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "9513", host = "127.0.0.1", port = "5432")
print("Conexão aberta com sucesso!")
cursor = conn.cursor()
fake = Faker('pt_BR')

n=10
for i in range(n):
    BRINCO = i+10
    SEXO = 'RECRIA_'+str(i+1)
    PESO = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(PESO)
    print(SEXO)

    comandoSQL = """ INSERT INTO PUBLIC. "RECRIA" ("BRINCO", "SEXO", "PESO") VALUES (%s, %s, %s)"""
    registro = (BRINCO, SEXO, PESO)
    cursor.execute(comandoSQL, registro)

conn.commit()
print("Inserção realizada com sucesso!");
conn.close()



class AppBD: # classe pra método CRUD
    def  __init__(self) :
        print  ('Método construtor')

    def abrirConexao (self) :
        try:
            self.connection = psycopg2.connect (user="postgres", password="9513", host="127.0.0.1", port="5432", database="postgres")
        except (Exception, psycopg2.Error) as error :
            if (self.connection) :
                print("Falha ao se conectar ao Banco de Dados", error)

    # Consultas
    
    def selecionarDados (self) :
        try:
            self.abrirConexao ()
            cursor = self.connection.cursor()

            print("Selecionando todos os animais")
            sql_select_query = """select * from public. "RECRIA" """

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)

        except (Exception, psycopg2.Error) as error:
            print("Erro ao selecionar operação", error)

        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com PostgreSQL foi fechada.")
        return registros
    
    #inserir dados

    def inserirDados(self, BRINCO, SEXO, PESO):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """ INSERT INTO public. "RECRIA" ("BRINCO", "SEXO", "PESO") VALUES (%s, %s, %s)"""
            record_to_insert = (BRINCO, SEXO, PESO)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print (count, "Registro inserido com sucesso na tabela RECRIA")
        except (Exception, psycopg2.Error) as error :
            if (self.connection) :
                print ("Falha ao inserir registro na tabela RECRIA", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# Atualizar dados
                
    def atualizarDados(self, BRINCO, SEXO, PESO):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()

            print("Registro Antes da Atualização")
            sql_select_query = """select * from public. "RECRIA" where "BRINCO" = %s"""
            cursor.execute(sql_select_query, (BRINCO,))
            record = cursor.fetchone()
            print(record)

            sql_update_query = """Update public. "RECRIA" set "NOME" = %s, "PESO" %s where "BRINCO" = %s"""
            cursor.execute(sql_update_query, (SEXO, PESO, BRINCO))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro após atualização")
            sql_select_query = """Select * from public. "RECRIA" where "BRINCO" = %s"""
            cursor.execute(sql_select_query, (BRINCO,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Erro de Atualização", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com PostgreSQL foi fechada.")

# Excluir dados
                
    def excluirDados(self, BRINCO):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sql_delete_query = """Delete from public. "RECRIA" where "BRINCO" = %s"""
            cursor.execute(sql_delete_query, (BRINCO,))

            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except (Exception, psycopg2.Error) as error:
            print("Erro na Exclusão", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreAQL foi fechada.")




    