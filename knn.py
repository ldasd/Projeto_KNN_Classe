class Knn:
    def __init__(self, k):
        self.k = k
    def __repr__(self):
        return(f'KNN parametro {self.k}')
    
    def fit(self,data):
        """
        Insere os dados do modelo treinado
        Parametro: Lista de dados classificados
        """
        self.data = data

    def distancia(self,l1,l2):
        """
        Calcula a distancia euclidiana de dois pontos 
        Parametro: l1 - lista referente ao ponto 1
                   l2 - lista referente ao ponto 2
        Retorno: Distancia
        """
        total = 0
        for x,y in (list(zip(l1,l2))):
            total += (x-y)**2
        total = total**(1/2)
        return(total) 
    
    def perfil_investidor(self,lista):
        """
        Define o perfil do investidor a partir da lista das N distancias
        Parametro: Lista das N distancias
        Retorno: Classificação
        """
        classif = {}
        for dados in lista:
            if classif.get(self.data[dados[1]][1],None) == None:
                classif[self.data[dados[1]][1]] = 1       
            else:
                classif[self.data[dados[1]][1]] += 1
        maior = 0
        classifica = ''
        for chave, valor in classif.items():
            if valor > maior:
                maior = valor
                classifica = chave            
        return (classifica)
    
    
    def predict(self,no_class):
        #self.no_class = no_class
        """
        Retorna a Classificação dos dados não Classificados
        Parametro: Lista de dados Não classificados
        Retorno: Dicionário com os dados Cadastrados
        """
        data_class = {}
        for cpf,_,valores in no_class:
            lista = []   
            for index, elemento in enumerate(self.data):
                dist = self.distancia(valores,elemento[2])
                lista.append((dist,index))
            lista = sorted(lista)
            data_class[cpf] = self.perfil_investidor(lista[0:self.k])
        return(data_class)

        

