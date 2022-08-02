class Veiculo:
    def __init__(self, placa):
        self.___placa = placa
        self._estacionado = False
        
    @property
    def placa(self):
        return self.___placa

    @property
    def estacionado(self):
        return self._estacionado
   
    @property
    def tipo (self):
        raise NotImplementedError()
   
    @estacionado.setter
    def estacionado(self, status):
        self.estacionado = status
            

    def estacionar(self):
        self.estacionado = True
       

    def sair_da_vaga(self):
        self.estacionado = False
        print(f'saindo da vaga com o carro {self.placa}')

    def __str__(self):
        tipo = 'Carro' if self.tipo == 2 else 'Moto'
        return f'Tipo: {tipo} Placa = {self.placa} estacionado: {self.estacionado} '

class Carro(Veiculo):

    def __ini__(self, placa):
        super.__init__(placa, self.estacionado, self.tipo)

    @property
    def tipo(self):
        return 2


class Moto (Veiculo):
    def __ini__(self, placa):
        super.__init__(placa,self.estacionado, self.tipo)

    @property
    def tipo(self):
        return 1


class Vaga:
    # 1 = moto
    # 2 = carro
    id = 0
    def __init__(self,  tamanho = 2, veiculo = Veiculo):
        self._tipo = 2
        self.livre = True
        self.placa = veiculo.placa
    #   indenticador  

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self,valor):
        if valor < 0 or valor > 2:
            raise ValueError()
        self._tipo = valor

    def ocupar(self,veiculo = Veiculo):

        # verificar se a vaga ta ocupada, verificar se ta ocupada ou nao
        self.livre = False
        if veiculo.tipo == 2 :
            Vaga.tipo = 0
        else:
            Vaga.tipo = 1
        veiculo.estacionar(veiculo)
        print(f'Ocupando a vaga de tipo {self.tipo} com o veiculo tipo {veiculo.tipo} e a placa {self.placa}')

    def desocupar(self):
        self.livre = True
        print(f'Desocupando a vaga')


    def __str__(self) -> str:
        status = 'Livre' if self.livre == True else 'Ocupada'
        return f'Vaga  Status: {status} Tipo:{self.tipo}\n'

class Estacionamento():
 
    vagas_em_uso = []
    count = 0
    
    def __init__(self):
        self.total_vagas = 10
        self.ultima_vaga_ocupada = 0

    def estacionar(self,veiculo, vaga = Vaga,):
        # instanciar vaga, comunicando vaga , indentificador

        if self.ultima_vaga_ocupada < 50 and len(Estacionamento.vagas_em_uso) < 50:
            self.ultima_vaga_ocupada += 1
            vaga_usada = self.ultima_vaga_ocupada
            vaga.ocupar(veiculo)
            print(f'Estacionando o veiculo {veiculo.placa} na vaga {vaga_usada}')
            par = [veiculo.placa,vaga_usada]  
            Estacionamento.vagas_em_uso.append(par)
            return  print(f'estacionado {veiculo.placa} na vaga {vaga_usada}')
        else:
            Estacionamento.count += 1
            return print(f'Estacionamento lotado, aguardando { Estacionamento.count}')

    def remover(self, veiculo, vaga = Vaga):

        # print(self.vagas_em_uso[0].index(carro.placa))

        for x  in Estacionamento.vagas_em_uso:
            try:
                find = veiculo.placa in x
                if find:
                    index = Estacionamento.vagas_em_uso.index(x)
                    self.vagas_em_uso.remove(x)
                    return print(f'Retirando veiculo {veiculo.placa}')
                    
            except Exception as e:
                print('não está no estacionamento')

        # if self.ultima_vaga_ocupada > 0:
        #     self.ultima_vaga_ocupada -= 1
           
        #     par = estacionamento.vagas_em_uso.index(veiculo.placa)
        #     vaga.desocupar(veiculo)
        #     print(f'Retirando o veiculo {veiculo.placa} da vaga {par}')
        #     if veiculo.placa in estacionamento.vagas_em_uso:
        #         estacionamento.vagas_em_uso.pop(estacionamento.vagas_em_uso.index(veiculo.placa))
        #     return  print(f'estacionado {veiculo.placa} na vaga {par}')
        # else:
        #     return print('Estacionamento vazio')


    def estado_do_estacionamento(self):
        print (f'----------------------------\n*** ESTACIONAMENTO INSTRUCT *** \n{self}\n----------------------------')


    def __str__(self):  

        total_ocupadas = int(len(Estacionamento.vagas_em_uso))
        total_livres =  self.total_vagas - total_ocupadas

        message1 = f'\n Vagas ocupadas: {total_ocupadas} Vagas livres: {total_livres} '

        message2 = f' Veiculos aguardando para estacionar: {self.total_vagas}'


        return ( '----LOTADO!----' + message2 + message1 ) if total_ocupadas == self.total_vagas else ( '----TEMOS VAGAS----' + message1)



e = Estacionamento()
v = Vaga()

carroAna = Carro(1212)
carroBia = Carro(5050)
moto1 = Moto(8989)

e.estacionar(carroAna)
e.estacionar(carroBia)

e.estado_do_estacionamento()

e.remover(carroAna)

e.estado_do_estacionamento()

e.estacionar(moto1)
e.estado_do_estacionamento()














        

