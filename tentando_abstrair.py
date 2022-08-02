

# from estacionamento import Estacionamento


class Veiculo():
    def __init__(self, placa):
        self.__placa = placa
        self._estacionado = False  ## 0 nao, 1 sim , 2 aguardando

    def estacionar(self,placa):
        self.estacionado = True
        return self

    def sair_vaga(self):
        self.estacionado = False

    @property
    def placa(self):
        return self.__placa

    @property
    def estacionado(self):
        return self._estacionado

    @estacionado.setter
    def estacionado(self, status):
        self._estacionado = status

    @property
    def tipo(self):
        raise NotImplementedError
    
    # @tipo.setter
    # def tipo(self, novo_tipo):
    #   self._tipo = novo_tipo

    def __str__(self):
        status = 'sim' if self.estacionado == True else 'não'
        return f'VEICULO --> Tipo:{self.tipo}  Placa:{self.placa} Estacionado:{status}'

class Carro(Veiculo):
    def __ini__(self):
        super().__init__()

    @property
    def tipo(self):
        return 'Carro'

class Moto(Veiculo):
    def __ini__(self):
        super().__init__()

    @property
    def tipo(self):
        return 'Moto'
       


class Vaga:
    tamanho_vaga = 2
    total_vagas = 10

    def __init__(self, veiculo = Veiculo):
        self.tipo = self.tamanho_vaga
        self.livre = True
        self.placa = ''
        self.ultima_vaga_usada = 0
        self.vagas = [self.abrir()]
       
 
    def abrir(self, veiculo = Veiculo):
        self.ultima_vaga_usada += 1 

        if self.ultima_vaga_usada < self.total_vagas:
            # self.vagas = [Vaga() for _ in range(self.total_vagas)]

            for i in range(Vaga.total_vagas):
                # vaga = veiculo.estacionar(veiculo.placa)
                return i
        else:
            print('NÃO HÁ VAGAS')   


    def estacionar(carro):
        for i in range(Vaga.vagas):
            vaga = Veiculo.estacionar()
            print(i,vaga)
            return i,vaga



    def __str__(self):
        tipo = 'Carro' if self.tipo == 2 else 'Moto'
        status = 'sim' if self.livre == False else 'não'
        placa = self.placa if self.placa else '--'
        return f'VAGA --> Tipo: {tipo}  Ocupada: {status}  Placa: {placa} -- '



v = Vaga()
carro = Carro(6565)
carro1 = Carro(8080)
carro2 = Carro(1212)

v.estacionar()

