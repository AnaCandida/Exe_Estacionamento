
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
        print(f'saindo da vaga com o veiculo {self.placa}')

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
    def __init__(self, tipo, identificador, veiculo = Veiculo):
        self._tipo = tipo
        self.livre = True
        self.placa = veiculo.placa
        self.identificador = identificador 

    @property
    def tipo(self):
        return self._tipo
   
    def ocupar(self,veiculo = Veiculo):

        # if self.livre == True:
        veiculo.estacionar(veiculo)
        print(f'Ocupando a vaga de tipo {self.tipo} com o veiculo tipo {veiculo.tipo} e a placa {self.placa}')
        # else:
        #     raise Exception('Vaga já está preenchida.')

    def desocupar(self):
        
        if self.livre == False:
            self.livre = True
            print(f'Desocupando a vaga')
        else:
            raise Exception('Vaga já está livre.')


    def __str__(self) -> str:
        status = 'Livre' if self.livre == True else 'Ocupada'
        return f'Vaga  Status: {status} Tipo:{self.tipo}\n'

class Estacionamento():
 
    vagas_em_uso_carros = []
    vagas_em_uso_motos = []
    aguardando_carro = 0
    aguardando_moto = 0    
    def __init__(self):
        self.total_vagas_carro = 10
        self.total_vagas_moto = 10
        self.total_vagas = self.total_vagas_carro + self.total_vagas_moto
        self.ultima_vaga_ocupada = 0

    def estacionar_carro(self,veiculo, vaga = Vaga,):
        if len(Estacionamento.vagas_em_uso_carros) < self.total_vagas_carro:
            self.ultima_vaga_ocupada += 1
            vaga_usada = self.ultima_vaga_ocupada
            v = Vaga(tipo =2 ,identificador = vaga_usada, veiculo = Veiculo)

            if veiculo.tipo != 2:
                raise Exception('Esta vaga aceita apenas carros.')
            
            vaga.ocupar(veiculo)
            print(f'Estacionando o veiculo {veiculo.placa} na vaga {vaga_usada}')
            par = [veiculo.placa,vaga_usada]  
            Estacionamento.vagas_em_uso_carros.append(par)
            return  print(f'{veiculo.placa}estacionado na vaga {vaga_usada}')
        else:
            Estacionamento.aguardando_carro += 1
            return print(f'Estacionamento sem vagas para carros, aguardando: { Estacionamento.aguardando_carro}')

    def remover_carro(self, veiculo, vaga = Vaga):

        for x  in Estacionamento.vagas_em_uso_carros:
            try:
                find = veiculo.placa in x
                if find:
                    index = Estacionamento.vagas_em_uso_carros.index(x)
                    self.vagas_em_uso_carros.remove(x)
                    return print(f'Retirando veiculo {veiculo.placa}')
                    
            except Exception as e:
                print('Não está no estacionamento')


    def estacionar_moto(self,veiculo, vaga = Vaga,):
            if len(Estacionamento.vagas_em_uso_motos) < self.total_vagas_moto:
                self.ultima_vaga_ocupada += 1
                vaga_usada = self.ultima_vaga_ocupada
                v = Vaga(tipo =2 ,identificador = vaga_usada, veiculo = Veiculo)

                if veiculo.tipo != 1:
                    raise Exception('Esta vaga aceita apenas motos.')
                
                vaga.ocupar(veiculo)
                print(f'Estacionando o veiculo {veiculo.placa} na vaga {vaga_usada}')
                par = [veiculo.placa,vaga_usada]  
                Estacionamento.vagas_em_uso_motos.append(par)
                return  print(f'{veiculo.placa} estacionado na vaga {vaga_usada}')
            else:
                Estacionamento.aguardando_moto += 1
                return print(f'Estacionamento sem vagas para motos, aguardando: { Estacionamento.aguardando_moto}')


    def remover_moto(self, veiculo, vaga = Vaga):

        for x  in Estacionamento.vagas_em_uso_motos:
            try:
                find = veiculo.placa in x
                if find:
                    index = Estacionamento.vagas_em_uso_motos.index(x)
                    self.vagas_em_uso_motos.remove(x)
                    return print(f'Retirando veiculo {veiculo.placa}')
                    
            except Exception as e:
                print('Não está no estacionamento')

    def estado_do_estacionamento(self):
        print (f'----------------------------\n*** ESTACIONAMENTO INSTRUCT *** \n{self}\n----------------------------')


    def __str__(self):  

        total_ocupadas_carros = int(len(Estacionamento.vagas_em_uso_carros))
        total_ocupadas_motos = int(len(Estacionamento.vagas_em_uso_motos))
        total_ocupadas = total_ocupadas_carros + total_ocupadas_motos

        total_livres_carros =   self.total_vagas_carro - total_ocupadas_carros
        total_livres_motos =  self.total_vagas_moto - total_ocupadas_motos
        
        message1 = f'\n Vagas ocupadas --> CARROS: {total_ocupadas_carros} MOTOS: {total_ocupadas_motos} \n Vagas livres --> CARROS {total_livres_carros} MOTOS:{total_livres_motos} '

        message2 = f' Veiculos aguardando para estacionar: Carros:{ Estacionamento.aguardando_carro} Moto: {Estacionamento.aguardando_moto}'

        if total_livres_carros == 0 and total_ocupadas < self.total_vagas:
            return f'SEM VAGAS LIVRES PARA CARROS----TEMOS VAGAS MOTOS-------Carros aguardando para estacionar: { Estacionamento.aguardando_carro} {message1}'
        if total_livres_motos == 0 and total_ocupadas < self.total_vagas:
            return f'SEM VAGAS LIVRES PARA MOTOS----TEMOS VAGAS CARROS-------Motos aguardando para estacionar: { Estacionamento.aguardando_moto} {message1}'

        return ( '----LOTADO!----' + message2 + message1 ) if total_ocupadas == self.total_vagas else ( '----TEMOS VAGAS----' + message1)


e = Estacionamento()

carroAna = Carro(1212)
carroBia = Carro(5050)
motoTiago = Moto(8989)

e.estacionar_carro(carroAna)
e.estacionar_carro(carroBia)
e.estacionar_moto(motoTiago)

e.estado_do_estacionamento()














        

