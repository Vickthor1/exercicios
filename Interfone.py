class Interfone:
    def __init__(self,modelo,endereco):
        self.modelo = modelo
        self.endereco = endereco
    
    def ligar_para_proprietario():
        a = a
    def registrar_chamada():
        b = b

class InterfoneResidencial(Interfone):
    def __init__(self, modelo, endereco,proprietario1,telefone1,proprietario2,telefone2,horario_da_ligacao,duracao_ligacao):
        super().__init__(modelo, endereco)
        self.proprietario1 = proprietario1
        self.proprietario2 = proprietario2
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.horario_da_ligacao = horario_da_ligacao
        self.duracao_ligacao = duracao_ligacao
        
    @classmethod
    def cadastro(cls):
        modelo = input("Qual é o modelo do interfone? ")
        endereco = input("Qual é o endereço? ")
        proprietario1 = input("Qual é o proprietario 1? ")
        telefone1 = input("Qual o telefone do proprietario 1? ")
        proprietario2 = input("Qual é o proprietario 2?")
        telefone2 = input("Qual o telefone do proprietario 2? ")
        horario_da_ligacao = input("Insira o horario da ligação? ")
        duracao_ligacao = input("Insira os minutos da ligação? ")
        return cls(modelo,endereco,proprietario1,telefone1,proprietario2,telefone2,horario_da_ligacao,duracao_ligacao)

    def ligar_para_proprietario(self):
        print(f"\nEndereço:{self.endereco}scolha um dos proprietaris para efetuar a ligação\n proprietario 1:{self.proprietario1}, com o telefone:{self.telefone1}\n proprietario 2:{self.proprietario2}, com o telefone:{self.telefone2}\n")
        while True:
            ligar = input("deseja ligar para qual proprietario? ")
            if ligar == "1" or ligar == "proprietario 1" or ligar == self.proprietario1 or ligar == self.telefone1:
                print(f"\nLigação para {self.proprietario1} foi efetuada com sucesso!\n")
                break
            elif ligar == "2" or ligar == "proprietario 2" or ligar == self.proprietario2 or ligar == self.telefone2:
                print(f"\nLigação para {self.proprietario2} foi efetuada com sucesso!\n")
                break
            else: 
                print("\n-não listado-\n")
                pass
    def registrar_chamada(self):
        
        print(f"\nChamada registrada para o endereço: {self.endereco}, no Horário: {self.horario_da_ligacao}, Duração: {self.duracao_ligacao} minutos\n")

interfonar1 = InterfoneResidencial("modelito","Morro do dende","José Couméia","22 998-072","Diego o maléfico","40028922","20:30","120")

interfonar1.ligar_para_proprietario()

interfonar1.registrar_chamada()

interfonar2 = InterfoneResidencial.cadastro()

interfonar2.ligar_para_proprietario()

interfonar2.registrar_chamada()