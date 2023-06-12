from cidades import Pais
import time


romenia = Pais()

romenia.add_cidade("Arad","Zerind",75)
romenia.add_cidade("Arad","Sibiu",140)
romenia.add_cidade("Arad","Timisoara",118)
romenia.add_cidade("Zerind","Oradea",71)
romenia.add_cidade("Oradea","Sibiu",151)
romenia.add_cidade("Timisoara","Lugoj",111)
romenia.add_cidade("Lugoj","Mechadia",70)
romenia.add_cidade("Mechadia","Drobeta",75)
romenia.add_cidade("Drobeta","Craiova",120)
romenia.add_cidade("Craiova","Pitesti",138)
romenia.add_cidade("Craiova","Rimnicu Vilcea",146)
romenia.add_cidade("Sibiu","Rimnicu Vilcea",80)
romenia.add_cidade("Rimnicu Vilcea","Pitesti",97)
romenia.add_cidade("Sibiu","Fagaras",99)
romenia.add_cidade("Fagaras","Bucharest",211)
romenia.add_cidade("Pitesti","Bucharest",101)
romenia.add_cidade("Bucharest","Giurgiu",90)
romenia.add_cidade("Bucharest","Urziceni",85)
romenia.add_cidade("Urziceni","Hirsova",98)
romenia.add_cidade("Hirsova","Eforie",86)
romenia.add_cidade("Urziceni","Vaslui",142)
romenia.add_cidade("Vaslui","Iasi",92)
romenia.add_cidade("Neamt","Iasi",87)

romenia.add_distancia_reta("Arad",366)
romenia.add_distancia_reta("Bucharest",0)
romenia.add_distancia_reta("Craiova",160)
romenia.add_distancia_reta("Drobeta",242)
romenia.add_distancia_reta("Eforie",161)
romenia.add_distancia_reta("Fagaras",176)
romenia.add_distancia_reta("Giurgiu",77)
romenia.add_distancia_reta("Hirsova",151)
romenia.add_distancia_reta("Iasi",226)
romenia.add_distancia_reta("Lugoj",244)
romenia.add_distancia_reta("Mehadia",241)
romenia.add_distancia_reta("Neamt",234)
romenia.add_distancia_reta("Oradea",380)
romenia.add_distancia_reta("Pitesti",100)
romenia.add_distancia_reta("Rimnicu Vilcea",193)
romenia.add_distancia_reta("Sibiu",253)
romenia.add_distancia_reta("Timisoara",329)
romenia.add_distancia_reta("Urziceni",80)
romenia.add_distancia_reta("Vaslui",199)
romenia.add_distancia_reta("Zerind",374)
fim =1 
while fim: 
    time.sleep(1)
    print("Menu")
    print("1 - Resultado Caminho de Arad para Bucharest com o Algoritmo Guloso")
    print("2 - Resultado Caminho de Arad para Bucharest com o Algoritmo A*")
    print("3 - Resultado Caminho de uma cidade que você queira para Bucharest com o Algoritmo Guloso")
    print("4 - Resultado Caminho de uma cidade que você queira para Bucharest com o Algoritmo A*")
    print("sair - para sair do programa")

    escolha = input("Entre com o valor desejado\n")
    if escolha == '1': 
        resultado = romenia.busca_gulosa("Arad","Bucharest")
        print(f"\n O menor caminho com o algoritmo GULOSO é: \n {resultado} \n")

    elif escolha == '2': 
        resultado = romenia.a_estrela("Arad","Bucharest")
        print(f"\n O menor caminho com o algoritmo A* é: \n {resultado} \n")
    elif escolha == '3': 
        nova_origem = input("Diga o novo local de origem")
        resultado = romenia.busca_gulosa(nova_origem,"Bucharest")
        print(f"\n O menor caminho com o algoritmo GULOSO é: \n {resultado} \n")
    elif escolha == '4': 
        nova_origem = input("Diga o novo local de origem")
        resultado = romenia.a_estrela(nova_origem,"Bucharest")
        print(f"\n O menor caminho com o algoritmo A* é: \n {resultado} \n")
    elif escolha == 'sair':
        fim = 0
    else: 
        print("Erro: Opção inexistente")


