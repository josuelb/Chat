class Pessoa(abs):
    def __init__(self, nome, sobrenome, dataNasc):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__dataNasc = dataNasc
    
    def __str__(self):
        return self.__nome, self.__sobrenome, self.__dataNasc
    
    def __repr__(self):
        return str(self)
    

class Usuarios(Pessoa):
    class Contatos:
        def __init__(self, nameuser, numero) -> None:
            self.__nameUser = nameuser
            self.__numero = numero
    
    def __init__(self, nome, sobrenome, dataNasc, numeroCell, usuario=None):
        super().__init__(nome, sobrenome, dataNasc)
        self.__usuario = usuario if usuario is not None else nome
        self.__numeroCell = numeroCell

        self.__contatos = []
    
    def __str__(self):
        return self.__usuario, self.__numeroCell, super().__str__()
    
    def __len__(self):
        return len(self.__contatos)
    
    def __setitem__(self, item: dict):
        for key, value in item:
            if self.__
    
    def __setcontato(self, numeroCell, nameuser):
        novoContato = self.Contatos(nameuser, numero=numeroCell)

        self.__contatos.append(novoContato)

