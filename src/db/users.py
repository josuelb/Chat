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
    
    def __init__(self, nome, sobrenome, dataNasc, numeroCell: int, usuario=None):
        super().__init__(nome, sobrenome, dataNasc)
        self.__usuario = usuario if usuario is not None else nome
        self.__numeroCell:int = numeroCell

        self.__contatos = []
    
    def __str__(self):
        return self.__usuario, self.__numeroCell, super().__str__()
    
    def __len__(self):
        return len(self.__contatos)
    
    def __iter__(self):
        for contato in self.__contatos:
            yield contato

    def getUser(self):
        return self.__usuario
    
    def getNum(self):
        return self.__numeroCell

    def setUser(self, name):
        if self.__usuario != name:
            self.__usuario = name
            return
        raise ValueError
    
    def getcontato(self, num: int= None, user=None):
        if num is not None:
            for i in self:
                if i.__numero == num:
                    return i
            return -1
        
        for value in self:
            if value.__nameUser == user or value.__numero == num:
                return value
        return -1
    
    def setcontato(self, numeroCell: int, nameuser):
        if self.getcontato(numeroCell) == -1:
            novoContato = self.Contatos(nameuser, numero=numeroCell)

            self.__contatos.append(novoContato)
            return
        
        raise IndexError

