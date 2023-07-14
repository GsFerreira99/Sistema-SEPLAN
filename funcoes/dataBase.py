from sqlalchemy import create_engine
import pandas as pd
import mysql.connector


class DataBase:

    def __init__(self, host, user, password, porta) -> None:
        self._host = host
        self._user = user
        self._porta = porta
        self._password = password

    def conectar(self):
        try:
            self._db = mysql.connector.connect(
                        host=self._host,
                        user=self._user,
                        password=self._password,
                        port=self._porta,
                        database="interfaceplanilha",
                        )
            self._cursor = self._db.cursor(buffered=True)
            self._engine = create_engine(f'mysql://{self._user}:{self._password}@{self._host}:{self._porta}/interfaceplanilha')
            self.drop_column()
            self.create_column_decreto_origem()
            self.create_column_decreto_destino()
            self.create_column_email_origem()
            self.create_column_email_destino()
            return "Conectado com sucesso."
        except mysql.connector.errors.DatabaseError as e:
            if e.errno == 1049:
                return self.criar_db()
            else:
                return e

    def drop_column(self):
        try:
            info = self._cursor.execute("""
            ALTER TABLE decretos DROP GERA_EMAIL""")
        except:
            pass
        try:
            info = self._cursor.execute("""
            ALTER TABLE decretos DROP PERMANECE_DECRETO""")
        except:
            pass

    def create_column_email_origem(self):
        try:
            info = self._cursor.execute("""
            SELECT `COLUMN_NAME`
            FROM `INFORMATION_SCHEMA`.`COLUMNS`
            WHERE `TABLE_SCHEMA`='interfaceplanilha'
            AND `TABLE_NAME`='decretos'
            AND `COLUMN_NAME`='NAO_GERA_EMAIL_ORIGEM';""")
            if info is None:
                self._cursor.execute("""
                    ALTER TABLE decretos
                    ADD COLUMN NAO_GERA_EMAIL_ORIGEM BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        except Exception as e:
            if e.msg == "Duplicate column name 'NAO_GERA_EMAIL_ORIGEM'":
                return 'NAO_GERA_EMAIL_ORIGEM Já Existe'
            self._cursor.execute("""
                ALTER TABLE decretos
                ADD COLUMN NAO_GERA_EMAIL_ORIGEM BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        return "Tabela 'NAO_GERA_EMAIL_ORIGEM' criada com sucesso."

    def create_column_email_destino(self):
        try:
            info = self._cursor.execute("""
            SELECT `COLUMN_NAME`
            FROM `INFORMATION_SCHEMA`.`COLUMNS`
            WHERE `TABLE_SCHEMA`='interfaceplanilha'
            AND `TABLE_NAME`='decretos'
            AND `COLUMN_NAME`='NAO_GERA_EMAIL_DESTINO';""")
            if info is None:
                self._cursor.execute("""
                    ALTER TABLE decretos
                    ADD COLUMN NAO_GERA_EMAIL_DESTINO BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        except Exception as e:
            if e.msg == "Duplicate column name 'NAO_GERA_EMAIL_DESTINO'":
                return 'NAO_GERA_EMAIL_DESTINO Já Existe'
            self._cursor.execute("""
                ALTER TABLE decretos
                ADD COLUMN NAO_GERA_EMAIL_DESTINO BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        return "Tabela 'NAO_GERA_EMAIL_DESTINO' criada com sucesso."

    def create_column_decreto_origem(self):
        try:
            info = self._cursor.execute("""
            SELECT `COLUMN_NAME`
            FROM `INFORMATION_SCHEMA`.`COLUMNS`
            WHERE `TABLE_SCHEMA`='interfaceplanilha'
            AND `TABLE_NAME`='decretos'
            AND `COLUMN_NAME`='PERMANECE_DECRETO_ORIGEM';""")
            if info is None:
                self._cursor.execute("""
                    ALTER TABLE decretos
                    ADD COLUMN PERMANECE_DECRETO_ORIGEM BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        except Exception as e:
            if e.msg == "Duplicate column name 'PERMANECE_DECRETO_ORIGEM'":
                return 'PERMANECE_DECRETO_ORIGEM Já Existe'
            self._cursor.execute("""
                ALTER TABLE decretos
                ADD COLUMN PERMANECE_DECRETO_ORIGEM BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        return "Tabela 'PERMANECE_DECRETO_ORIGEM' criada com sucesso."

    def create_column_decreto_destino(self):
        try:
            info = self._cursor.execute("""
            SELECT `COLUMN_NAME`
            FROM `INFORMATION_SCHEMA`.`COLUMNS`
            WHERE `TABLE_SCHEMA`='interfaceplanilha'
            AND `TABLE_NAME`='decretos'
            AND `COLUMN_NAME`='PERMANECE_DECRETO_DESTINO';""")
            if info is None:
                self._cursor.execute("""
                    ALTER TABLE decretos
                    ADD COLUMN PERMANECE_DECRETO_DESTINO BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        except Exception as e:
            if e.msg == "Duplicate column name 'PERMANECE_DECRETO_DESTINO'":
                return 'PERMANECE_DECRETO_DESTINO Já Existe'
            self._cursor.execute("""
                ALTER TABLE decretos
                ADD COLUMN PERMANECE_DECRETO_DESTINO BOOLEAN DEFAULT FALSE AFTER STATUS_3_DESTINO;""")
        return "Tabela 'PERMANECE_DECRETO_DESTINO' criada com sucesso."

    def criar_db(self):
        db = mysql.connector.connect(
                        host=self._host,
                        user=self._user,
                        port=self._porta,
                        password=self._password,
                        )
        cursor = db.cursor()
        try:
            cursor.execute("CREATE DATABASE interfaceplanilha")
            self.conectar()
            self.criar_tabela()
            return 'Banco de Dados criado com sucesso.'
        except mysql.connector.errors.DatabaseError as e:
            return e

    def criar_tabela(self):
        try:
            self._cursor.execute("""CREATE TABLE decretos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                N_DECRETO VARCHAR(255), 
                DOTACAO_SUPLEMENTADA VARCHAR(255),
                DOTACAO_ANULADO VARCHAR(255),
                VALOR_FINANCEIRO VARCHAR(255),
                VALOR_FISICO_ATUAL_SUPLEMENTADO VARCHAR(255),
                VALOR_FISICO_ATUAL_ANULADO VARCHAR(255),
                DATA_ALTERACAO_ORCAMENTARIA DATE,
                NOME_ORGAO_SUPLEMENTADO VARCHAR(255),
                UNIDADE_SUPLEMENTADO VARCHAR(255),
                NOME_ORGAO_SUPLEMENTADO2 VARCHAR(255),
                FUCAO_SUPLEMENTADO VARCHAR(255),
                SUBFUNCAO_SUPLEMENTADO VARCHAR(255),
                ID_PROGRAMA_SUPLEMENTADO VARCHAR(255),
                PROGRAMA_SUPLEMENTADO VARCHAR(255),
                ID_ACAO_SUPLEMENTADO VARCHAR(255),
                ACAO_SUPLEMENTADO VARCHAR(255),
                NATUREZA_DA_DESPESA_SUPLEMENTADO VARCHAR(255),
                FONTE_DE_RECURSO_SUPLEMENTADO VARCHAR(255),
                NOME_PRODUTO_SUPLEMENTADO VARCHAR(255),
                ORGAO_ANULADO VARCHAR(255),
                UNIDADE_ANULADO VARCHAR(255),
                NOME_ORGAO_ANULADO VARCHAR(255),
                FUNCAO_ANULADO VARCHAR(255),
                SUBFUNCAO_ANULADO VARCHAR(255),
                ID_PROGRAMA_ANULADO VARCHAR(255),
                PROGRAMA_ANULADO VARCHAR(255),
                ID_ACAO_ANULADO VARCHAR(255),
                ACAO_ANULADO VARCHAR(255),
                NATUREZA_DA_DESPEZA_ANULADA VARCHAR(255),
                FONTE_DE_RECURSO_ANULADA VARCHAR(255),
                NOME_PRODUTO_ANULADO VARCHAR(255),
                OCORRIDO VARCHAR(255),
                COL_ALERTA VARCHAR(255),
                DATA_EMAIL_INICIAL DATE,
                EMAIL_INICIAL VARCHAR(255),
                EMAIL_ENVIADO VARCHAR(255),
                NOVA_META_FISICA_ANULADO VARCHAR(255),
                NOVA_META_FISICA_SUPLEMENTADO VARCHAR(255),
                INSERIDO_METAS VARCHAR(255),
                ATUALIZADO_NO_SISTEMA VARCHAR(255),
                DATA_CONTATO_1_ORIGEM DATE,
                CONTATO_1_ORIGEM VARCHAR(255),
                STATUS_1_ORIGEM VARCHAR(255),
                DATA_CONTATO_2_ORIGEM DATE,
                CONTATO_2_ORIGEM VARCHAR(255),
                STATUS_2_ORIGEM VARCHAR(255),
                DATA_CONTATO_3_ORIGEM DATE,
                CONTATO_3_ORIGEM VARCHAR(255),
                STATUS_3_ORIGEM VARCHAR(255),
                DATA_CONTATO_1_DESTINO DATE,
                CONTATO_1_DESTINO VARCHAR(255),
                STATUS_1_DESTINO VARCHAR(255),
                DATA_CONTATO_2_DESTINO DATE,
                CONTATO_2_DESTINO VARCHAR(255),
                STATUS_2_DESTINO VARCHAR(255),
                DATA_CONTATO_3_DESTINO DATE,
                CONTATO_3_DESTINO VARCHAR(255),
                STATUS_3_DESTINO VARCHAR(255)
                )""")
        except mysql.connector.errors.ProgrammingError as e:
            return e
        return "Tabela 'decretos' criada com sucesso."

    def inserir_decreto(self, val):
        sql = """INSERT INTO decretos (
            N_DECRETO,
            DOTACAO_SUPLEMENTADA,
            DOTACAO_ANULADO,
            VALOR_FINANCEIRO,
            VALOR_FISICO_ATUAL_SUPLEMENTADO,
            VALOR_FISICO_ATUAL_ANULADO,
            DATA_ALTERACAO_ORCAMENTARIA,
            NOME_ORGAO_SUPLEMENTADO,
            UNIDADE_SUPLEMENTADO,
            NOME_ORGAO_SUPLEMENTADO2,
            FUCAO_SUPLEMENTADO,
            SUBFUNCAO_SUPLEMENTADO,
            ID_PROGRAMA_SUPLEMENTADO,
            PROGRAMA_SUPLEMENTADO,
            ID_ACAO_SUPLEMENTADO,
            ACAO_SUPLEMENTADO,
            NATUREZA_DA_DESPESA_SUPLEMENTADO,
            FONTE_DE_RECURSO_SUPLEMENTADO,
            NOME_PRODUTO_SUPLEMENTADO,
            ORGAO_ANULADO,
            UNIDADE_ANULADO,
            NOME_ORGAO_ANULADO,
            FUNCAO_ANULADO,
            SUBFUNCAO_ANULADO,
            ID_PROGRAMA_ANULADO,
            PROGRAMA_ANULADO,
            ID_ACAO_ANULADO,
            ACAO_ANULADO,
            NATUREZA_DA_DESPEZA_ANULADA,
            FONTE_DE_RECURSO_ANULADA,
            NOME_PRODUTO_ANULADO,
            OCORRIDO,
            COL_ALERTA,
            DATA_EMAIL_INICIAL,
            EMAIL_INICIAL,
            EMAIL_ENVIADO,
            NOVA_META_FISICA_ANULADO,
            NOVA_META_FISICA_SUPLEMENTADO,
            INSERIDO_METAS,
            ATUALIZADO_NO_SISTEMA,
            DATA_CONTATO_1_ORIGEM,
            CONTATO_1_ORIGEM,
            STATUS_1_ORIGEM,
            DATA_CONTATO_2_ORIGEM,
            CONTATO_2_ORIGEM,
            STATUS_2_ORIGEM,
            DATA_CONTATO_3_ORIGEM,
            CONTATO_3_ORIGEM,
            STATUS_3_ORIGEM,
            DATA_CONTATO_1_DESTINO,
            CONTATO_1_DESTINO,
            STATUS_1_DESTINO,
            DATA_CONTATO_2_DESTINO,
            CONTATO_2_DESTINO,
            STATUS_2_DESTINO,
            DATA_CONTATO_3_DESTINO,
            CONTATO_3_DESTINO,
            STATUS_3_DESTINO
            ) 
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        self._cursor.executemany(sql, val)
        self._db.commit()
        return "Dados importados com sucesso."

    def atualizar_decreto(self, val):
        sql = """
        UPDATE 
            decretos 
        SET 
            VALOR_FISICO_ATUAL_ANULADO = %s,
            VALOR_FISICO_ATUAL_SUPLEMENTADO = %s,
            DATA_EMAIL_INICIAL = %s,
            EMAIL_INICIAL = %s,
            DATA_CONTATO_1_ORIGEM = %s,
            CONTATO_1_ORIGEM = %s,
            STATUS_1_ORIGEM = %s,
            DATA_CONTATO_2_ORIGEM = %s,
            CONTATO_2_ORIGEM = %s,
            STATUS_2_ORIGEM = %s,
            DATA_CONTATO_3_ORIGEM = %s,
            CONTATO_3_ORIGEM = %s,
            STATUS_3_ORIGEM = %s,
            DATA_CONTATO_1_DESTINO = %s,
            CONTATO_1_DESTINO = %s,
            STATUS_1_DESTINO = %s,
            DATA_CONTATO_2_DESTINO = %s,
            CONTATO_2_DESTINO = %s,
            STATUS_2_DESTINO = %s,
            DATA_CONTATO_3_DESTINO = %s,
            CONTATO_3_DESTINO = %s,
            STATUS_3_DESTINO = %s,
            NOVA_META_FISICA_ANULADO = %s,
            NOVA_META_FISICA_SUPLEMENTADO = %s,
            EMAIL_ENVIADO = %s,
            INSERIDO_METAS = %s,
            ATUALIZADO_NO_SISTEMA = %s,
            NAO_GERA_EMAIL_ORIGEM = %s,
            NAO_GERA_EMAIL_DESTINO = %s,
            PERMANECE_DECRETO_ORIGEM = %s,
            PERMANECE_DECRETO_DESTINO = %s
        WHERE 
            id = %s"""

        self._cursor.execute(sql, val)
        self._db.commit()
    def atualizar_decreto_espelhado(self, val):
        try:
            if type(val['metaOrigemAtual']) is list:
                v = val['metaOrigemAtual'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    VALOR_FISICO_ATUAL_ANULADO = %s
                WHERE 
                    id = %s
                    """
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['geraEmailOrigem']) is list:
                v = val['geraEmailOrigem'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    NAO_GERA_EMAIL_ORIGEM = %s
                WHERE 
                    id = %s
                    """
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['geraEmailDestino']) is list:
                v = val['geraEmailDestino'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    NAO_GERA_EMAIL_DESTINO = %s
                WHERE 
                    id = %s
                    """
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['permaneceMetaOrigem']) is list:
                v = val['permaneceMetaOrigem'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    PERMANECE_DECRETO_ORIGEM = %s,
                    NOVA_META_FISICA_ANULADO = 'permanece a mesma meta'
                WHERE 
                    id = %s
                    """
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['permaneceMetaDestino']) is list:
                v = val['permaneceMetaDestino'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    PERMANECE_DECRETO_DESTINO = %s,
                    NOVA_META_FISICA_SUPLEMENTADO = 'permanece a mesma meta'
                WHERE 
                    id = %s
                    """
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['metaDestinoAtual']) is list:
                v = val['metaDestinoAtual'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    VALOR_FISICO_ATUAL_SUPLEMENTADO = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['metaOrigemSuplementado']) is list:
                v = val['metaOrigemSuplementado'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    NOVA_META_FISICA_ANULADO = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['metaDestinoSuplementado']) is list:
                v = val['metaDestinoSuplementado'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    NOVA_META_FISICA_SUPLEMENTADO = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['dataEmail']) is list:
                v = val['dataEmail'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    DATA_EMAIL_INICIAL = %s,
                    EMAIL_INICIAL = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['emailOrigem']) is list:
                v = val['emailOrigem'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    DATA_CONTATO_1_ORIGEM = %s,
                    CONTATO_1_ORIGEM = %s,
                    STATUS_1_ORIGEM = %s,
                    DATA_CONTATO_2_ORIGEM = %s,
                    CONTATO_2_ORIGEM = %s,
                    STATUS_2_ORIGEM = %s,
                    DATA_CONTATO_3_ORIGEM = %s,
                    CONTATO_3_ORIGEM = %s,
                    STATUS_3_ORIGEM = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['emailDestino']) is list:
                v = val['emailDestino'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    DATA_CONTATO_1_DESTINO = %s,
                    CONTATO_1_DESTINO = %s,
                    STATUS_1_DESTINO = %s,
                    DATA_CONTATO_2_DESTINO = %s,
                    CONTATO_2_DESTINO = %s,
                    STATUS_2_DESTINO = %s,
                    DATA_CONTATO_3_DESTINO = %s,
                    CONTATO_3_DESTINO = %s,
                    STATUS_3_DESTINO = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['statusEnviado']) is list:
                v = val['statusEnviado'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    EMAIL_ENVIADO = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['statusMetas']) is list:
                v = val['statusMetas'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    INSERIDO_METAS = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        try:
            if type(val['statusSistema']) is list:
                v = val['statusSistema'] + val['id']
                sql = """
                UPDATE 
                    decretos 
                SET 
                    ATUALIZADO_NO_SISTEMA = %s
                WHERE 
                    id = %s"""
                self._cursor.execute(sql, v)
        except Exception as e:
            print(e)
        self._db.commit()

    def select_busca(self, campo, tela):
        
        if len(campo) == 2:
            if tela == 'TODOS':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s",params={'ini':campo[0], 'fim': campo[1]}, con=self._engine)
            elif tela == 'ANÁLISE':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO != 'ok' AND COL_ALERTA != 'OK') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s",params={'ini':campo[0], 'fim': campo[1]}, con=self._engine)
            elif tela == 'EMAIL ENVIADO':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO = 'ok') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s",params={'ini':campo[0], 'fim': campo[1]}, con=self._engine)
            elif tela == 'METAS INSERIDAS':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE (INSERIDO_METAS = 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s",params={'ini':campo[0], 'fim': campo[1]}, con=self._engine)
            elif tela == 'INSERIDO SISTEMA':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE ATUALIZADO_NO_SISTEMA = 'ok' AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s",params={'ini':campo[0], 'fim': campo[1]}, con=self._engine)

        else:
            try:
                int(campo[0])
                if len(campo[0]) == 2:
                    campo = f"{campo[0]}"
                else:
                    campo = f"%{campo[0]}"
            except:
                campo = f"%{campo[0]}%"

            if tela == 'TODOS':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE N_DECRETO LIKE %(campo)s OR \
                    DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                    ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ORGAO_ANULADO LIKE %(campo)s OR \
                    NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                    ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                    PROGRAMA_ANULADO LIKE %(campo)s OR \
                    ID_ACAO_ANULADO LIKE %(campo)s OR \
                    ACAO_ANULADO LIKE %(campo)s",params={'campo':campo}, con=self._engine)
            elif tela == 'ANÁLISE':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO != 'ok' AND COL_ALERTA != 'OK') AND (N_DECRETO LIKE %(campo)s OR \
                    DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                    ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ORGAO_ANULADO LIKE %(campo)s OR \
                    NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                    ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                    PROGRAMA_ANULADO LIKE %(campo)s OR \
                    ID_ACAO_ANULADO LIKE %(campo)s OR \
                    ACAO_ANULADO LIKE %(campo)s)",params={'campo':campo}, con=self._engine)
            elif tela == 'EMAIL ENVIADO':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE ((INSERIDO_METAS != 'ok' OR INSERIDO_METAS is null) AND (ATUALIZADO_NO_SISTEMA != 'ok' OR ATUALIZADO_NO_SISTEMA is null) AND EMAIL_ENVIADO = 'ok') AND (N_DECRETO LIKE %(campo)s OR \
                    DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                    ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ORGAO_ANULADO LIKE %(campo)s OR \
                    NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                    ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                    PROGRAMA_ANULADO LIKE %(campo)s OR \
                    ID_ACAO_ANULADO LIKE %(campo)s OR \
                    ACAO_ANULADO LIKE %(campo)s)",params={'campo':campo}, con=self._engine)
            elif tela == 'METAS INSERIDAS':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE INSERIDO_METAS = 'ok' AND (ATUALIZADO_NO_SISTEMA != 'ok' OR ATUALIZADO_NO_SISTEMA is null) AND (N_DECRETO LIKE %(campo)s OR \
                    DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                    ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ORGAO_ANULADO LIKE %(campo)s OR \
                    NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                    ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                    PROGRAMA_ANULADO LIKE %(campo)s OR \
                    ID_ACAO_ANULADO LIKE %(campo)s OR \
                    ACAO_ANULADO LIKE %(campo)s)",params={'campo':campo}, con=self._engine)
            elif tela == 'INSERIDO SISTEMA':
                q = pd.read_sql(
                "SELECT * FROM decretos WHERE ATUALIZADO_NO_SISTEMA = 'ok' AND (N_DECRETO LIKE %(campo)s OR \
                    DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                    NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                    ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                    ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                    ORGAO_ANULADO LIKE %(campo)s OR \
                    NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                    ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                    PROGRAMA_ANULADO LIKE %(campo)s OR \
                    ID_ACAO_ANULADO LIKE %(campo)s OR \
                    ACAO_ANULADO LIKE %(campo)s )",params={'campo':campo}, con=self._engine)

        return q

    def busca_espelhamento(self, campo, tela, decreto):
        sql = ''
        if len(campo) == 2:
            if tela == 'TODOS':
                sql = "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s"
            elif tela == 'ANÁLISE':
                sql = "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO != 'ok' AND COL_ALERTA != 'OK') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s"
            elif tela == 'EMAIL ENVIADO':
                sql = "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO = 'ok') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s"
            elif tela == 'METAS INSERIDAS':
                sql = "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND (INSERIDO_METAS = 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok') AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s"
            elif tela == 'INSERIDO SISTEMA':
                sql = "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND ATUALIZADO_NO_SISTEMA = 'ok' AND DATA_ALTERACAO_ORCAMENTARIA BETWEEN %(ini)s AND %(fim)s"
            q = pd.read_sql(
                f"{sql}",
                params={'ini': campo[0], 'fim': campo[1], 'decreto': decreto}, con=self._engine)
        else:
            try:
                int(campo[0])
                if len(campo[0]) == 2:
                    campo = f"{campo[0]}"
                else:
                    campo = f"%{campo[0]}"
            except:
                campo = f"%{campo[0]}%"


            if tela == 'ANÁLISE':
                q = pd.read_sql(
                    "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND (INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO != 'ok' AND COL_ALERTA != 'OK') AND \
                        (DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                        ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ORGAO_ANULADO LIKE %(campo)s OR \
                        NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                        ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                        PROGRAMA_ANULADO LIKE %(campo)s OR \
                        ID_ACAO_ANULADO LIKE %(campo)s OR \
                        ACAO_ANULADO LIKE %(campo)s)", params={'campo': campo, 'decreto': int(decreto)}, con=self._engine)
            elif tela == 'EMAIL ENVIADO':
                q = pd.read_sql(
                    "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND ((INSERIDO_METAS != 'ok' OR INSERIDO_METAS is null) AND (ATUALIZADO_NO_SISTEMA != 'ok' OR ATUALIZADO_NO_SISTEMA is null) AND EMAIL_ENVIADO = 'ok') AND \
                        (DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                        ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ORGAO_ANULADO LIKE %(campo)s OR \
                        NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                        ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                        PROGRAMA_ANULADO LIKE %(campo)s OR \
                        ID_ACAO_ANULADO LIKE %(campo)s OR \
                        ACAO_ANULADO LIKE %(campo)s)", params={'campo': campo, 'decreto': int(decreto)},
                    con=self._engine)
            elif tela == 'METAS INSERIDAS':
                q = pd.read_sql(
                    "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND INSERIDO_METAS = 'ok' AND (ATUALIZADO_NO_SISTEMA != 'ok' OR ATUALIZADO_NO_SISTEMA is null) AND \
                        (DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                        ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ORGAO_ANULADO LIKE %(campo)s OR \
                        NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                        ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                        PROGRAMA_ANULADO LIKE %(campo)s OR \
                        ID_ACAO_ANULADO LIKE %(campo)s OR \
                        ACAO_ANULADO LIKE %(campo)s)", params={'campo': campo, 'decreto': int(decreto)},
                    con=self._engine)
            elif tela == 'INSERIDO SISTEMA':
                q = pd.read_sql(
                    "SELECT * FROM decretos WHERE N_DECRETO = %(decreto)s AND  ATUALIZADO_NO_SISTEMA = 'ok' AND \
                        (DATA_ALTERACAO_ORCAMENTARIA LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO LIKE %(campo)s OR \
                        NOME_ORGAO_SUPLEMENTADO2 LIKE %(campo)s OR \
                        ID_PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        PROGRAMA_SUPLEMENTADO LIKE %(campo)s OR \
                        ID_ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ACAO_SUPLEMENTADO LIKE %(campo)s OR \
                        ORGAO_ANULADO LIKE %(campo)s OR \
                        NOME_ORGAO_ANULADO LIKE %(campo)s OR \
                        ID_PROGRAMA_ANULADO LIKE %(campo)s OR \
                        PROGRAMA_ANULADO LIKE %(campo)s OR \
                        ID_ACAO_ANULADO LIKE %(campo)s OR \
                        ACAO_ANULADO LIKE %(campo)s)", params={'campo': campo, 'decreto': int(decreto)},
                    con=self._engine)
        return q

    def select_decreto(self, id):
        d = pd.read_sql(f"SELECT * FROM decretos WHERE id = {id}", con=self._engine)
        return d.loc[0]

    @property
    def select_todos(self):
        d = pd.read_sql("SELECT * FROM decretos ORDER BY DATA_ALTERACAO_ORCAMENTARIA DESC", con=self._engine)
        return d
    
    @property
    def select_analise(self):
        return pd.read_sql("SELECT * FROM decretos WHERE INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO != 'ok' AND COL_ALERTA != 'OK' ORDER BY DATA_ALTERACAO_ORCAMENTARIA DESC", con=self._engine)

    @property
    def select_email(self):
        return pd.read_sql("SELECT * FROM decretos WHERE INSERIDO_METAS != 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' AND EMAIL_ENVIADO = 'ok' ORDER BY DATA_ALTERACAO_ORCAMENTARIA DESC", con=self._engine)
    
    @property
    def select_metas(self):
        return pd.read_sql("SELECT * FROM decretos WHERE INSERIDO_METAS = 'ok' AND ATUALIZADO_NO_SISTEMA != 'ok' ORDER BY DATA_ALTERACAO_ORCAMENTARIA DESC", con=self._engine)

    @property
    def select_inserido(self):
        return pd.read_sql("SELECT * FROM decretos WHERE ATUALIZADO_NO_SISTEMA = 'ok' ORDER BY DATA_ALTERACAO_ORCAMENTARIA DESC", con=self._engine)

    @property
    def select_secretarias(self):
        return pd.read_sql("SELECT DISTINCT NOME_ORGAO_SUPLEMENTADO2 FROM decretos",con=self._engine)

    @property
    def select_score_1(self):
        email = pd.read_sql("SELECT COUNT(INSERIDO_METAS) FROM decretos WHERE INSERIDO_METAS='ok'", con=self._engine)
        todos = pd.read_sql("SELECT COUNT(N_DECRETO) FROM decretos", con=self._engine)

        return int(email.iloc[0]['COUNT(INSERIDO_METAS)']) / int(todos.iloc[0]['COUNT(N_DECRETO)'])

    @property
    def select_score_2(self):
        email = pd.read_sql("SELECT COUNT(EMAIL_ENVIADO) FROM decretos WHERE EMAIL_ENVIADO='ok'", con=self._engine)
        todos = pd.read_sql("SELECT COUNT(N_DECRETO) FROM decretos", con=self._engine)

        return int(email.iloc[0]['COUNT(EMAIL_ENVIADO)'])/int(todos.iloc[0]['COUNT(N_DECRETO)'])

    def select_filtro_score_2(self, filtro: str):
        email = pd.read_sql(
            f"SELECT COUNT(INSERIDO_METAS) FROM decretos WHERE INSERIDO_METAS='ok' AND (NOME_ORGAO_SUPLEMENTADO2 = '{filtro}' OR NOME_ORGAO_ANULADO = '{filtro}')", con=self._engine)
        todos = pd.read_sql(
            f"SELECT COUNT(N_DECRETO) FROM decretos WHERE NOME_ORGAO_SUPLEMENTADO2 = '{filtro}' OR NOME_ORGAO_ANULADO = '{filtro}'", con=self._engine)

        return int(email.iloc[0]['COUNT(INSERIDO_METAS)']) / int(todos.iloc[0]['COUNT(N_DECRETO)'])

    def select_filtro_score_1(self, filtro: str):
        email = pd.read_sql(f"SELECT COUNT(EMAIL_ENVIADO) FROM decretos WHERE EMAIL_ENVIADO='ok'  AND (NOME_ORGAO_SUPLEMENTADO2 = '{filtro}' OR NOME_ORGAO_ANULADO = '{filtro}')", con=self._engine)
        todos = pd.read_sql(f"SELECT COUNT(N_DECRETO) FROM decretos WHERE NOME_ORGAO_SUPLEMENTADO2 = '{filtro}' OR NOME_ORGAO_ANULADO = '{filtro}'", con=self._engine)

        return int(email.iloc[0]['COUNT(EMAIL_ENVIADO)']) / int(todos.iloc[0]['COUNT(N_DECRETO)'])

