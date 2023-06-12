

class Pais: 
    def __init__(self): #contrutor de um grafo vazio 
        self.grafo = {}
        self.distancia_reta = {}
    
    def add_cidade (self,origem,destino,distancia):
        if origem not in self.grafo:
            self.grafo[origem]=[]
        if destino not in self.grafo:
            self.grafo[destino]=[]

        self.grafo[origem].append((destino,distancia))
        self.grafo[destino].append((origem,distancia))
    
    def add_distancia_reta(self,origem,distancia):
        self.distancia_reta[origem] = distancia

    def get_vizinhos(self,vertice):
        return self.grafo.get(vertice,[])
    def get_distancia_reta(self,cidade):
        return self.distancia_reta[cidade]
    
    def busca_gulosa (pais,origem,destino):
        if origem not in pais.grafo:
            print("Cidades não encontradas.")
            return
        caminho = []
        visitadas = set()

        caminho.append(origem)
        while caminho[-1] != destino: 
            vizinhos = pais.get_vizinhos(caminho[-1])
            #ordena as cidades de menor distancia reta 
            vizinhos.sort(key=lambda cidade: pais.get_distancia_reta(cidade[0])) 
            for vizinho in vizinhos:
                cidade = vizinho[0]
                distancia = pais.get_distancia_reta(cidade)
                if cidade not in visitadas:
                    caminho.append(cidade)
                    visitadas.add(cidade)
                    break

        return caminho
    

    def a_estrela(pais, origem, destino):
        if origem not in pais.grafo:
            print("Cidades não encontradas.")
            return
        caminho = []
        visitadas = set()

        caminho.append(origem)
        atual = origem
        while caminho[-1] != destino: 
            vizinhos = pais.get_vizinhos(caminho[-1])
            #ordena as cidades de menor distancia reta 
            vizinhos.sort(key=lambda cidade: pais.get_distancia_reta(cidade[0])) 
            menor_custo = [99999,"Numero Grande"] #numero maior que as distancias existentes no grafo
            for vizinho in vizinhos:
                
                cidade = vizinho[0]
                distancia = pais.get_distancia_reta(cidade)
                custo = [vizinho[1] + distancia,cidade] #aqui ele leva em consideração as duas distancias 
                if custo < menor_custo:
                    menor_custo[0]=custo[0]
                    menor_custo[1]=custo[1]

            if menor_custo[1] not in visitadas:
                    atual = menor_custo[1]
                    caminho.append(menor_custo[1])
                    visitadas.add(menor_custo[1])
                    

        return caminho