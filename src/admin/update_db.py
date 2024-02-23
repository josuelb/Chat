from .config import mydb

"""
Esse modulo vai ser responsavel por ser o intermediario entre banco de dados, interface e api.

Ele vai atualizar, resgatar e gernciar informações do banco de dados.
"""
cur = mydb.cursor()


class DataBase:
    def createTable():
        try:
            cur.execute("""
CREATE TABLE contatos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomeUser VARCHAR(50), 
    numero INT
)
""")
            
            cur.execute("""
CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    sobrenome VARCHAR(100),
    dataNasc DATE,
    usuario VARCHAR(50),
    numeroCell INT,
    contatos INT,
    FOREIGN KEY (contatos) REFERENCES contatos(numero)
)
""")
        except:
            raise ConnectionError
    
    def get(dado: int=None):
        try:
            if dado is not None:
                cur.execute(f"SELECT * FROM usuarios WHERE numeroCell = {dado}")
            else:
                cur.execute("SELECT * FROM usuarios")
            
            data = cur.fetchall()
            cur.close()
            return data
        except:
            DataBase.createTable()
    
    def set(dado: dict):
        pass